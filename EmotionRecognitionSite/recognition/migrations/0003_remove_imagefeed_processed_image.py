# Generated by Django 5.1.2 on 2024-11-01 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0002_detectedobject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagefeed',
            name='processed_image',
        ),
    ]
