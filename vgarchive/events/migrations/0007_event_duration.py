# Generated by Django 5.1.1 on 2024-09-18 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(days=5), verbose_name='Duration'),
            preserve_default=False,
        ),
    ]
