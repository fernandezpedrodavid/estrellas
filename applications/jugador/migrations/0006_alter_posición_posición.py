# Generated by Django 4.1.3 on 2022-12-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0005_remove_jugador_sueldo_anual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posición',
            name='posición',
            field=models.CharField(choices=[('0', 'Arquero'), ('1', 'Defensor'), ('2', 'Medio campo'), ('3', 'Delantero')], max_length=3, verbose_name='Posición'),
        ),
    ]
