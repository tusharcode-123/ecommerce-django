# Generated by Django 4.1.4 on 2022-12-08 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cartitem_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variationitem',
        ),
    ]
