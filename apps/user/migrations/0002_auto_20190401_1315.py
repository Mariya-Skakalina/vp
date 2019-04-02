# Generated by Django 2.1.2 on 2019-04-01 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='user',
            name='partner',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Партнер'),
        ),
    ]
