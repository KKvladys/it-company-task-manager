from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Worker, Position


# Register your models here.
@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)


admin.site.register(Position)
