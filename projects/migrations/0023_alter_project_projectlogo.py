# Generated by Django 3.2.4 on 2021-07-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20210719_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectlogo',
            field=models.FileField(blank=True, upload_to='documents/', verbose_name='Research Paper'),
        ),
    ]
