# Generated by Django 3.2.4 on 2021-08-10 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210801_1739'),
        ('forum', '0008_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.RemoveField(
            model_name='message',
            name='downvoters',
        ),
        migrations.RemoveField(
            model_name='message',
            name='thread',
        ),
        migrations.RemoveField(
            model_name='message',
            name='upvoters',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='author',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='prefix',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='thread',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='authentication.profile'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
        migrations.DeleteModel(
            name='ThreadPrefix',
        ),
    ]
