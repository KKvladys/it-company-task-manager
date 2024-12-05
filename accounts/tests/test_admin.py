from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tasks.models import Position


class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="12345",
            email="admin_mail@www.com"
        )
        test_position = Position.objects.create(name="Test")
        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="test_password",
            email="test_mail@www.com",
            position=test_position
        )

    def test_driver_position_listed(self):
        """
        Test check worker position is in list_display on
        worker admin page
        """
        url = reverse("admin:accounts_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)