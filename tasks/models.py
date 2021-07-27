from django.db import models
from .task_priority import moderate, task_priority
from .task_status import undone, status_choice


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=task_priority, default=moderate)
    status = models.CharField(max_length=10, choices=status_choice, default=undone)
