# Generated by Django 2.0.dev20170510134720 on 2017-11-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidad', '0006_consultas_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='genero',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Género'),
        ),
    ]