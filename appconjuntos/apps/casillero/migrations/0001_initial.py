# Generated by Django 4.0.4 on 2022-06-06 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conjunto', '0002_alter_conjuntomodel_email_alter_conjuntomodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasilleroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vacio', models.BooleanField(default=False, verbose_name='Esta vacio?')),
                ('is_active', models.BooleanField(default=True)),
                ('fk_propiedad', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='conjunto.conjuntomodel')),
            ],
            options={
                'verbose_name': 'Casillero',
                'verbose_name_plural': 'Casilleros',
            },
        ),
    ]
