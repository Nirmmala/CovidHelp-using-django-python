# Generated by Django 4.1 on 2022-09-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='availability',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
