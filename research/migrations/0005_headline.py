# Generated by Django 3.2.4 on 2021-07-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_alter_research_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
    ]
