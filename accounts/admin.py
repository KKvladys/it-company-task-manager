from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Worker


# Register your models here.
@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    