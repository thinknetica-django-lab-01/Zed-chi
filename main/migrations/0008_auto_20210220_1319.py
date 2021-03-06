# Generated by Django 3.1.4 on 2021-02-20 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210220_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='создано'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='обновлено'),
        ),
    ]
