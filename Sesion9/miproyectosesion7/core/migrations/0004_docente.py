# Generated by Django 5.0.4 on 2024-05-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_carrera_codigo_alter_carrera_duracion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField()),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('titulo', models.CharField(max_length=20, verbose_name='Titulo')),
            ],
        ),
    ]