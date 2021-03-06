# Generated by Django 3.2.4 on 2021-06-21 14:43

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=150)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitee', to=settings.AUTH_USER_MODEL)),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
