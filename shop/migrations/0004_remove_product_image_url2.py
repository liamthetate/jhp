# Generated by Django 3.2 on 2022-04-10 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_image_url2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url2',
        ),
    ]
