# Generated by Django 3.0.2 on 2020-02-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_juego'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='hora',
        ),
        migrations.AddField(
            model_name='juego',
            name='jugador',
            field=models.ManyToManyField(to='jobs.Jugador'),
        ),
    ]
