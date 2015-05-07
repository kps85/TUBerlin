# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20150505_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 13, 52, 21, 69553), verbose_name='Task published'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 11, 52, 21, 69553, tzinfo=utc), verbose_name='Task deadline'),
        ),
    ]
