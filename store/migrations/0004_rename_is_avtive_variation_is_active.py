# Generated by Django 4.1.4 on 2022-12-08 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_variation_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='is_avtive',
            new_name='is_active',
        ),
    ]
