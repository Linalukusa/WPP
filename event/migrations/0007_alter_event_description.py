# Generated by Django 3.2.4 on 2021-08-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20210814_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]