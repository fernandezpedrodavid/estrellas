# Generated by Django 4.1.3 on 2022-12-28 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0004_jugador_sueldo_anual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='sueldo_anual',
        ),
    ]
