# Generated by Django 2.2.10 on 2020-06-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceimage',
            options={'verbose_name': 'Imagem', 'verbose_name_plural': 'Imagens'},
        ),
        migrations.AlterField(
            model_name='service',
            name='datetime',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
