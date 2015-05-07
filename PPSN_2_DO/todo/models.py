import datetime

from django.db import models
from django.utils import timezone

class Task(models.Model):
    TASK_STATUS = (
        ('C', 'Cancelled'),
        ('D', 'Done'),
        ('I', 'Important'),
        ('R', 'Running'),
    )

    pub_date = models.DateTimeField("Task published", default=timezone.now)
    task_deadline = models.DateField("Task deadline", default=datetime.datetime.now)
    task_desc = models.CharField("Task description", max_length=500)
    task_progress = models.PositiveSmallIntegerField("Task progress", default=0)
    task_status = models.CharField("Task status", max_length=1, choices=TASK_STATUS, default="R")

    def __str__(self):
        return self.task_desc

# Create your models here.
