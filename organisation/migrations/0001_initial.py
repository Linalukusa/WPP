# Generated by Django 3.2.4 on 2021-08-05 03:24

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisationname', models.CharField(max_length=500, verbose_name='Organisation Name')),
                ('city', models.CharField(blank=True, max_length=500, verbose_name='City')),
                ('projectlogo', models.FileField(blank=True, upload_to='documents/', verbose_name='Research Paper')),
                ('website', models.URLField(blank=True, verbose_name='Website')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Email')),
                ('mission', ckeditor.fields.RichTextField(verbose_name='Mission')),
                ('vision', models.TextField(verbose_name='Vision')),
                ('achieved', models.TextField(verbose_name='What We Have Achieved?')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='OrganisationParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.organisation')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
