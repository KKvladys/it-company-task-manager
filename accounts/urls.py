from django.urls import path, include

from accounts.views import WorkerListView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("/workers/", WorkerListView.as_view(), name="worker-list")
    # path("register/", WorkerCreateView.as_view(), name="register")
]

app_name = "accounts"