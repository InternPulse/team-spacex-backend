# Generated by Django 5.0.1 on 2024-01-24 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicepilot_app', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
