# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateTimeField(verbose_name='Task deadline', default=datetime.datetime(2015, 5, 5, 11, 7, 22, 767008, tzinfo=utc)),
        ),
    ]
