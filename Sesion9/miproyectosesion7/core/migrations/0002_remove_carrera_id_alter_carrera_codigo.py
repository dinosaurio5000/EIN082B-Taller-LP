# Generated by Django 5.0.4 on 2024-05-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrera',
            name='id',
        ),
        migrations.AlterField(
            model_name='carrera',
            name='codigo',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
