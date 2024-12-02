from django.urls import path, include

from accounts.views import WorkerListView, WorkerDetailView

app_name = "accounts"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("/workers/", WorkerListView.as_view(), name="worker-list"),
    path("<int:pk>/", WorkerDetailView.as_view(), name="worker-detail")
    # path("register/", WorkerCreateView.as_view(), name="register")
]
