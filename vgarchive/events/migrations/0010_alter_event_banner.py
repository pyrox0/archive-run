# Generated by Django 5.1.1 on 2024-09-20 20:00

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_rename_end_datetime_event_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='event-banners/'),
        ),
    ]
