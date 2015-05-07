# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_auto_20150505_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 13, 54, 53, 305397), verbose_name='Task published'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Task deadline'),
        ),
    ]
