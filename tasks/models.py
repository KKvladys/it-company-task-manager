from django.conf import settings
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        (0, "Urgent"),
        (1, "High"),
        (2, "Medium"),
        (3, "Low"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(
        TaskType,
        related_name="tasks",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    class Meta:
        ordering = ("priority", "deadline",)

    def __str__(self):
        return self.name
