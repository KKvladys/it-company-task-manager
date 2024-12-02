from django.urls import path

from tasks.views import (
    index,
    TaskListView,
    TaskDtailView,
    TaskHistoryListView
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/history/", TaskHistoryListView.as_view(), name="task-list-history"),
    path("<int:pk>/tasks/", TaskDtailView.as_view(), name="task-detail")
]

app_name = "tasks"