# Generated by Django 5.0.6 on 2024-06-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_responsecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='img_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='responsecomment',
            name='img',
            field=models.TextField(null=True),
        ),
    ]
