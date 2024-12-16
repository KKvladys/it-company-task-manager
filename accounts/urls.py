from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts.views import (
    WorkerListView,
    WorkerDetailView,
    WorkerUpdateView,
    WorkerDeleteView,
    register_user
)

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LogoutView.as_view(next_page='/login/'), name="login"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("register/", register_user, name="register")
]
