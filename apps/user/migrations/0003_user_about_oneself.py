# Generated by Django 2.1.2 on 2019-04-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190401_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_oneself',
            field=models.TextField(blank=True, null=True),
        ),
    ]
