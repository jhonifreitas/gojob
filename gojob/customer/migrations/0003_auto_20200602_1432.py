# Generated by Django 2.2.10 on 2020-06-02 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200602_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='datetime',
            new_name='date',
        ),
    ]
