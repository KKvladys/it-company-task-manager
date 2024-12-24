from django.urls import path

from tasks import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/tasks/", views.TaskDtailView.as_view(), name="task-detail"),
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>",
        views.ChangeTaskStatusView.as_view(),
        name="task-change-status",
    ),
    path("task-types/", views.TaskTypeListView.as_view(), name="task-type-list"),
    path(
        "task-types/create/",
        views.TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "task-types/<int:pk>/update/",
        views.TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task-types/<int:pk>/delete/",
        views.TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
    path(
        "task-types/<int:pk>/detail/",
        views.TaskTypeDetailView.as_view(),
        name="task-type-detail",
    ),
    path(
        "tasks/history/", views.TaskHistoryListView.as_view(), name="task-list-history"
    ),
]

app_name = "tasks"
