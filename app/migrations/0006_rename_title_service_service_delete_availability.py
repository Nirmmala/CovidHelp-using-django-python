# Generated by Django 4.1 on 2022-09-16 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_facility_service_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='title',
            new_name='service',
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
    ]
