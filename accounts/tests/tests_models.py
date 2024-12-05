from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelsTest(TestCase):
    def test_worker_str(self):
        worker = get_user_model().objects.create_user(
            username="testuser",
            password="strongpassword",
            first_name="Test",
            last_name="User",
        )
        self.assertEqual(str(worker), f"{worker.first_name} {worker.last_name}")
