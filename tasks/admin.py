from django.contrib import admin

from tasks.models import TaskType, Task


admin.site.register(TaskType)
admin.site.register(Task)
