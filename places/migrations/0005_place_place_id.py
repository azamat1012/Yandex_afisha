# Generated by Django 5.1.7 on 2025-03-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_remove_image_image_urls_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
