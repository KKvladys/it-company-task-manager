from django.urls import path

from tasks.views import (
    home,
    TaskListView,
    TaskDtailView,
    TaskHistoryListView,
    TaskUpdateView,
    TaskDeliteView,
    TaskCreateView,
    PositionCreateView,
    TaskTypeCreateView,
    TaskTypeListView,
    PositionListView


)

urlpatterns = [
    path("", home, name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/list/", PositionCreateView.as_view(), name="position-create"),
    path("task-types/", TaskTypeListView.as_view(),name="task-type-list"),
    path("task-types/create/", TaskTypeCreateView.as_view(),name="task-type-create"),
    path("tasks/history/", TaskHistoryListView.as_view(), name="task-list-history"),
    path("<int:pk>/tasks/", TaskDtailView.as_view(), name="task-detail"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeliteView.as_view(), name="task-delite")
]

app_name = "tasks"
