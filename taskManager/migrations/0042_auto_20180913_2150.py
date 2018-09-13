# Generated by Django 2.1.1 on 2018-09-13 21:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0041_auto_20160429_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 21, 50, 58, 896124, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 21, 50, 58, 897082, tzinfo=utc), verbose_name='date due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='N/A', max_length=1024),
        ),
    ]