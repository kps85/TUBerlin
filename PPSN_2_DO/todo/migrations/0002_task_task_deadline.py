# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_deadline',
            field=models.DateTimeField(verbose_name='Task deadline', default=datetime.datetime(2015, 5, 5, 10, 22, 28, 41523, tzinfo=utc)),
        ),
    ]
