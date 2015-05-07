# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20150505_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 11, 47, 31, 147246, tzinfo=utc), verbose_name='Task published'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(default=datetime.datetime(2015, 5, 5, 13, 47, 31, 147246), verbose_name='Task deadline'),
        ),
    ]
