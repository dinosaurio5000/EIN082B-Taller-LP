# Generated by Django 5.0.4 on 2024-05-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=200)),
                ('duracion', models.IntegerField()),
            ],
        ),
    ]