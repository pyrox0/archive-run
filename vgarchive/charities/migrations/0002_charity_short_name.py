# Generated by Django 5.1 on 2024-08-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='short_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Short Name'),
        ),
    ]
