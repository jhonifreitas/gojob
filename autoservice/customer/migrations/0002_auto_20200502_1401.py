# Generated by Django 2.2.10 on 2020-05-02 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expiration',
            field=models.DateField(blank=True, default=datetime.date(2020, 7, 31), null=True, verbose_name='Expiração'),
        ),
    ]
