# Generated by Django 3.2.4 on 2021-07-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20210716_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectlogo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='Project Logo'),
        ),
    ]
