# Generated by Django 5.1.1 on 2024-09-20 20:10

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charities', '0007_alter_charity_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='icon',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='charity-banners/', verbose_name='Icon/Favicon'),
        ),
    ]
