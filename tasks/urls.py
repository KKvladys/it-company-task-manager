from django.urls import path

from tasks.views import (
    home,
    TaskListView,
    TaskDtailView,
    TaskHistoryListView
)

urlpatterns = [
    path("", home, name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/history/", TaskHistoryListView.as_view(), name="task-list-history"),
    path("<int:pk>/tasks/", TaskDtailView.as_view(), name="task-detail")
]

app_name = "tasks"
