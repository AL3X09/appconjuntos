# Generated by Django 4.0.4 on 2022-07-06 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_noticiamodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticiamodel',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
    ]
