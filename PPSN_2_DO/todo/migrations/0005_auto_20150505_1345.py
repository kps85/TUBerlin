# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20150505_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 13, 45, 48, 496275), verbose_name='Task deadline'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(verbose_name='Task status', max_length=1, choices=[('C', 'Cancelled'), ('D', 'Done'), ('I', 'Important'), ('R', 'Running')], default='R'),
        ),
    ]
