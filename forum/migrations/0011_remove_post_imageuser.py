# Generated by Django 3.2.4 on 2021-08-10 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_rename_image_post_imageuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imageuser',
        ),
    ]
