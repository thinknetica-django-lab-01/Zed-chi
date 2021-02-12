from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField("название", max_length=50)
    description = models.TextField("описание", max_length=300, blank=True)
    price = models.DecimalField("цена", max_digits=8, decimal_places=2)
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)
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

