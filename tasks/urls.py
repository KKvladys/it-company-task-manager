from django.urls import path

from tasks import views


urlpatterns = [
    path("",  views.home, name="home"),
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/tasks/", views.TaskDtailView.as_view(), name="task-detail"),
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", views.TaskDeliteView.as_view(), name="task-delite"),
    path("tasks/<int:pk>", views.change_task_status, name="task-change-status"),
    path("positions/", views.PositionListView.as_view(), name="position-list"),
    path("positions/create/", views.PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/delete", views.PositionDeleteView.as_view(), name="position-delete"),
    path("positions/<int:pk>/detail/", views.PositionDetailView.as_view(), name="position-detail"),
    path("positions/<int:pk>/update/", views.PositionUpdateView.as_view(), name="position-update"),
    path("task-types/", views.TaskTypeListView.as_view(),name="task-type-list"),
    path("task-types/create/", views.TaskTypeCreateView.as_view(),name="task-type-create"),
    path("task-types/<int:pk>/update/", views.TaskTypeUpdateView.as_view(),name="task-type-update"),
    path("task-types/<int:pk>/delete/", views.TaskTypeDeleteView.as_view(),name="task-type-delete"),
    path("task-types/<int:pk>/detail/", views.TaskTypeDetailView.as_view(),name="task-type-detail"),
    path("tasks/history/", views.TaskHistoryListView.as_view(), name="task-list-history"),

]

app_name = "tasks"
