# Generated by Django 4.2.5 on 2024-01-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_listings_images_listings_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='contact',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
