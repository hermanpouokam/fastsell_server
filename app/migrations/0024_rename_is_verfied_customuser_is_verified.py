# Generated by Django 5.0.6 on 2024-06-13 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_rename_certified_customuser_is_certified_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_verfied',
            new_name='is_verified',
        ),
    ]