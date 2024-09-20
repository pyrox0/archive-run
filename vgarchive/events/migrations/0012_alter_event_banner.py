# Generated by Django 5.1.1 on 2024-09-20 20:29

import imagekit.models.fields
import vgarchive.events.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_event_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=vgarchive.events.models._upload_banner, verbose_name='Banner Image'),
        ),
    ]
