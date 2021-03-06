# Generated by Django 3.2.4 on 2021-07-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20210715_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='achieved',
            field=models.TextField(verbose_name='What We Have Achieved?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='city',
            field=models.CharField(blank=True, max_length=500, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='project',
            name='enddate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='howwedo',
            field=models.TextField(verbose_name='How We Do?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='linkedin',
            field=models.URLField(blank=True, max_length=500, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='project',
            name='maintheme',
            field=models.CharField(max_length=500, verbose_name='Main Theme'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectlogo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Project Logo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectsummary',
            field=models.TextField(verbose_name='Project Summary'),
        ),
        migrations.AlterField(
            model_name='project',
            name='province',
            field=models.IntegerField(blank='false', choices=[(1, 'Select'), (2, ' Eastern Cape'), (3, 'Free State'), (4, 'Gauteng'), (5, 'KwaZulu-Natal'), (6, 'Limpopo'), (7, 'Mpumalanga'), (8, 'Northern Cape'), (9, 'North West'), (10, 'Western Cape'), (11, 'All nationals'), (12, 'International')], default=1, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='project',
            name='startdate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='topic',
            field=models.CharField(max_length=500, verbose_name='Topic'),
        ),
        migrations.AlterField(
            model_name='project',
            name='website',
            field=models.URLField(blank=True, max_length=500, verbose_name='Website'),
        ),
        migrations.AlterField(
            model_name='project',
            name='whatwedo',
            field=models.TextField(verbose_name='What We Do?'),
        ),
    ]
