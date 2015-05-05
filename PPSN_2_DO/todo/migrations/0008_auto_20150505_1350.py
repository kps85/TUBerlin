# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20150505_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Task published'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(verbose_name='Task deadline'),
        ),
    ]
