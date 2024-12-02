from django.urls import path

from tasks.views import (
    index,
    TaskListView,
    TaskDtailView
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/tasks/", TaskDtailView.as_view(), name="task-detail")
]

app_name = "tasks"