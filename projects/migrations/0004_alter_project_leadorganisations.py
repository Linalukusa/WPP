# Generated by Django 3.2.4 on 2021-06-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_bachieved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='leadorganisations',
            field=models.CharField(default='', max_length=500),
        ),
    ]
