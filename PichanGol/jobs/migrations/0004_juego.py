# Generated by Django 3.0.2 on 2020-02-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200210_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Realizado', 'Realizado'), ('Cancelado', 'Cancelado')], max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Cancha')),
            ],
        ),
    ]
