# Generated by Django 4.0.4 on 2022-06-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conjunto', '0003_rename_imagen_conjuntomodel_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conjuntomodel',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='../front_vue/public/img/conjunto/', verbose_name='Imagen del conjunto'),
        ),
        migrations.AlterField(
            model_name='conjuntomodel',
            name='logo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='../front_vue/public/img/conjunto/', verbose_name='Logo del conjunto'),
        ),
    ]
