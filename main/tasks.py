from celery import Celery
from celery.task import PeriodicTask
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from main.models import Subscriber, Product
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.template import loader
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.models import Site

app = Celery()
logger = get_task_logger(__name__)
   

@app.task
def send_new_product_letter(product):
    logger.info("Sent new product")
    for subscription in Subscriber.objects.all():
        email = subscription.user.email
        name = subscription.user.username
        message = f"""
            Добрый день {name}.
            У нас в продаже появился новый продукт: {product.name}.
            Для просмотра пройдите по ссылке www.{Site.objects.get_current().domain}{reverse("main:good_detail", args=[product.id,])} .
        """
        send_mail(
            "Поступление новых продуктов",message,"",[email,]
        )
