# Generated by Django 4.1.3 on 2022-12-27 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugador', '0002_alter_país_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posición',
            name='posición',
            field=models.CharField(choices=[('Arq', 'Arquero'), ('Def', 'Defensor'), ('Med', 'Medio campo'), ('Del', 'Delantero')], max_length=3, verbose_name='Posición'),
        ),
    ]
