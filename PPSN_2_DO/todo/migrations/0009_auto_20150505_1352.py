# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20150505_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Task published', default=datetime.datetime(2015, 5, 5, 11, 52, 7, 738235, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(verbose_name='Task deadline', default=datetime.datetime(2015, 5, 5, 13, 52, 7, 738235)),
        ),
    ]
