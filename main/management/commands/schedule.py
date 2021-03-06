import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from main.models import Subscriber, Product
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.shortcuts import render
from django.template import loader


logger = logging.getLogger(__name__)


def my_job():
    week_ago = timezone.now() - timedelta(days=7)
    products_of_the_week = Product.objects.filter(created_on__gt=week_ago)
    if not products_of_the_week:
        return
    content = loader.render_to_string("./week_update.html",{"products":products_of_the_week}, None)
    for subscribe in Subscriber.objects.all():
        send_mail("Товары недели", content, None, [subscribe.user.email,])    


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
                
        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")