# Generated by Django 4.1 on 2022-09-15 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_availability_available_availability_total'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Facility',
            new_name='Service',
        ),
        migrations.RenameField(
            model_name='availability',
            old_name='facility',
            new_name='service',
        ),
    ]