# Generated by Django 3.2.4 on 2021-07-18 11:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_alter_project_projectlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectsummary',
            field=ckeditor.fields.RichTextField(verbose_name='Project Summary'),
        ),
    ]
