# Generated by Django 2.0.dev20170510134720 on 2017-10-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
    ]