from celery import Celery
from celery.task import PeriodicTask
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from main.models import Subscriber, Product
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.template import loader

app = Celery()
logger = get_task_logger(__name__)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):    
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        send_week_updates.s(),
    )

@app.task
def send_week_updates():
    logger.info("Sent new products of the week")
    week_ago = timezone.now() - timedelta(days=7)
    products_of_the_week = Product.objects.filter(created_on__gt=week_ago)
    if not products_of_the_week:
        return
    content = loader.render_to_string("./week_update.html",{"products":products_of_the_week}, None)
    for subscribe in Subscriber.objects.all():
        send_mail("Товары недели", content, None, [subscribe.user.email,])    
