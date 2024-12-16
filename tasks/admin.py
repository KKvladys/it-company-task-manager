from django.contrib import admin

from tasks.models import TaskType, Position, Task


admin.site.register(TaskType)
admin.site.register(Position)
admin.site.register(Task)
