# Generated by Django 3.2.4 on 2021-07-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_remove_project_projectlogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectlogo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
