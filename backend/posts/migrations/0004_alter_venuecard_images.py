# Generated by Django 5.0 on 2024-02-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_image_url_venuecard_location_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venuecard',
            name='images',
            field=models.FileField(blank=True, default='', max_length=255, null=True, upload_to=''),
        ),
    ]
