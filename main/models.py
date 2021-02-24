from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.models import Site
from django.utils import timezone



class Product(models.Model):
    name = models.CharField("название", max_length=50)
    description = models.TextField("описание", max_length=300, blank=True)
    price = models.DecimalField("цена", max_digits=8, decimal_places=2)
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)
    created_on = models.DateTimeField("создано", default=timezone.now, db_index=True,)
    updated_on = models.DateTimeField("обновлено", null=True, blank=True, db_index=True,)
    category = models.ForeignKey(
        "ProductCategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        related_name="products",
    )
    tags = models.ManyToManyField("Tag")

    STATUSES = [
        ("A", "Available"),
        ("N", "Not Available"),
    ]
    status = models.CharField(choices=STATUSES, default="A", max_length=20)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(
        "картинка",
        upload_to="./product_images",
    )
    product = models.ForeignKey(
        "Product",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="фото",
        related_name="images",
    )


class ProductCategory(models.Model):
    name = models.CharField("название", max_length=50)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField("тег", max_length=50)

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.title


class Seller(User):
    company_name = models.CharField("название", max_length=50)
    description = models.TextField(
        max_length=500,
        null=False,
        blank=True,
    )

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

class Subscriber(models.Model):    
    user = models.ForeignKey(User, related_name="subscribtions", on_delete=models.CASCADE)

# TODO написать сигнал подписки на обновления

@receiver(post_save, sender=Product)
def notify(sender, instance, **kwargs):
    for subscription in Subscriber.objects.all():
        print(instance)
        email = subscription.user.email
        name = subscription.user.username
        message = f"""
            Добрый день {name}.
            У нас в продаже появился новый продукт: {instance.name}.
            Для просмотра пройдите по ссылке www.{Site.objects.get_current().domain}{reverse("main:good_detail", args=[instance.id,])} .
        """
        send_mail(
            "Поступление новых продуктов",message,"",[email,]
        )
