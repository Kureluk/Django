# Generated by Django 5.1.4 on 2025-01-24 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='birthdate',
        ),
    ]
