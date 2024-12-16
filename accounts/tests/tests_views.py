from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from tasks.models import Position

User = get_user_model()


class WorkerViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(name="Software Engineer")
        self.worker = User.objects.create_user(
            username="testworker",
            password="password123",
            email="worker@example.com",
            first_name="Test",
            last_name="Worker",
            position=self.position
        )
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
            email="admin@example.com"
        )

    def test_worker_list_view(self):
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(reverse("accounts:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.worker.username)

    def test_worker_detail_view(self):
        self.client.login(username="admin", password="adminpassword")
        response = self.client.get(reverse("accounts:worker-detail", args=[self.worker.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.worker.first_name)
        self.assertContains(response, self.worker.last_name)

    def test_worker_update_view(self):
        self.client.login(username="admin", password="adminpassword")
        response = self.client.post(reverse("accounts:worker-update", args=[self.worker.id]), {
            "first_name": "Updated",
            "last_name": "Name",
            "position": self.position.id
        })
        self.assertEqual(response.status_code, 302)
        self.worker.refresh_from_db()
        self.assertEqual(self.worker.first_name, "Updated")
        self.assertEqual(self.worker.last_name, "Name")


class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.worker = User.objects.create_user(
            username="testworker",
            password="password123"
        )

    def test_login_valid(self):
        response = self.client.post(reverse("accounts:login"), {
            "username": "testworker",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    def test_login_invalid(self):
        response = self.client.post(reverse("accounts:login"), {
            "username": "testworker",
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, 200)
