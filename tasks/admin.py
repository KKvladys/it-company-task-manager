from django.contrib import admin

from tasks.models import TaskType, Position

# Register your models here.

admin.site.register(TaskType)
admin.site.register(Position)