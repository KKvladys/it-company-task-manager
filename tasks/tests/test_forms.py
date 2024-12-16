from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils.timezone import now

from tasks.forms import TaskForm, TaskTypeForm, PositionForm
from tasks.models import TaskType

User = get_user_model()


class TaskFormTests(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Development")
        self.user1 = User.objects.create_user(
            username="user1",
            password="password123",
            email="user1@example.com"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="password123",
            email="user2@example.com"
        )

        self.valid_data = {
            "name": "Fix login bug",
            "task_type": self.task_type.pk,
            "is_completed": False,
            "description": "Fix the login bug for all users.",
            "deadline": (now() + timedelta(days=7)).date(),
            "priority": 0,
            "assignees": [self.user1.pk, self.user2.pk]
        }

    def test_task_form_valid(self):
        form = TaskForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_task_form_missing_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data["name"] = ""
        form = TaskForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_task_form_invalid_deadline(self):
        invalid_data = self.valid_data.copy()
        invalid_data["deadline"] = "invalid-date"
        form = TaskForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("deadline", form.errors)

    def test_task_form_missing_assignees(self):
        invalid_data = self.valid_data.copy()
        invalid_data["assignees"] = []
        form = TaskForm(data=invalid_data)
        self.assertFalse(form.is_valid())


class TaskTypeFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Bug Fixing"
        }

    def test_task_type_form_valid(self):
        form = TaskTypeForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_task_type_form_missing_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data["name"] = ""
        form = TaskTypeForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class PositionFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Software Engineer"
        }

    def test_position_form_valid(self):
        form = PositionForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_position_form_missing_name(self):
        invalid_data = self.valid_data.copy()
        invalid_data["name"] = ""
        form = PositionForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
