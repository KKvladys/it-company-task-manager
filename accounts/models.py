from django.contrib.auth.models import AbstractUser
from django.db import models

from tasks.models import Position


class Worker(AbstractUser):
    email = models.EmailField(unique=True)
    position = models.ForeignKey(
        Position,
        related_name="workers",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
