# Generated by Django 3.2.4 on 2021-08-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_alter_project_projectlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectlogo',
            field=models.FileField(blank=True, upload_to='documents/', verbose_name='Research Paper'),
        ),
    ]
