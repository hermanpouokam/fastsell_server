# Generated by Django 5.0.6 on 2024-06-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_tag_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_first_login',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='uid',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
