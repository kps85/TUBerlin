# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_auto_20150505_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Task published', default=datetime.datetime(2015, 5, 5, 13, 55, 36, 490269)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(verbose_name='Task deadline', default=datetime.datetime.now),
        ),
    ]
