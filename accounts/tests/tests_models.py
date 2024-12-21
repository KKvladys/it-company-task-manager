from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import Position


class ModelsTest(TestCase):
    def test_worker_str(self):
        worker = get_user_model().objects.create_user(
            username="testuser",
            password="strongpassword",
            first_name="Test",
            last_name="User",
        )
        self.assertEqual(str(worker), f"{worker.first_name} {worker.last_name}")


class PositionModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Software Engineer")

    def test_position_str(self):
        self.assertEqual(str(self.position), "Software Engineer")
