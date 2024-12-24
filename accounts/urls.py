from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts import views

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("workers/", views.WorkerListView.as_view(), name="worker-list"),
    path("<int:pk>/", views.WorkerDetailView.as_view(), name="worker-detail"),
    path("<int:pk>/update/", views.WorkerUpdateView.as_view(), name="worker-update"),
    path("<int:pk>/delete/", views.WorkerDeleteView.as_view(), name="worker-delete"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("positions/", views.PositionListView.as_view(), name="position-list"),
    path(
        "positions/create/", views.PositionCreateView.as_view(), name="position-create"
    ),
    path(
        "positions/<int:pk>/delete",
        views.PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path(
        "positions/<int:pk>/detail/",
        views.PositionDetailView.as_view(),
        name="position-detail",
    ),
    path(
        "positions/<int:pk>/update/",
        views.PositionUpdateView.as_view(),
        name="position-update",
    ),
]
