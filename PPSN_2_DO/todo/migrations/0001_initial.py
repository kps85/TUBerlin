# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='Task published')),
                ('task_desc', models.CharField(verbose_name='Task description', max_length=500)),
                ('task_progress', models.PositiveSmallIntegerField(default=0, verbose_name='Task progress')),
                ('task_status', models.CharField(verbose_name='Task status', choices=[('C', 'Cancelled'), ('D', 'Done'), ('I', 'Important'), ('R', 'Running')], max_length=1)),
            ],
        ),
    ]
