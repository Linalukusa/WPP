# Generated by Django 3.2.4 on 2021-07-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_alter_research_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
        ),
    ]
