# Generated by Django 4.1 on 2022-09-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_availability_available_availability_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='available',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='availability',
            name='total',
            field=models.IntegerField(default=''),
        ),
    ]
