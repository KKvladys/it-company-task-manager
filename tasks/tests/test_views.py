from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils.timezone import now

from tasks.models import Task, Position, TaskType


class TaskViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )

        self.task_type = TaskType.objects.create(name="Development")

        self.task = Task.objects.create(
            name="Test Task",
            task_type=self.task_type,
            is_completed=False,
            description="Test task description",
            deadline=now() + timedelta(days=7),
            priority=0
        )

        self.client.login(username='testuser', password='password123')

    def test_home_view(self):
        response = self.client.get(reverse("tasks:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/home.html")
        self.assertIn("num_task_urgent", response.context)
        self.assertIn("num_task_high", response.context)

    def test_task_list_view(self):
        response = self.client.get(reverse("tasks:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_list.html")
        self.assertContains(response, "Test Task")

    def test_task_detail_view(self):
        response = self.client.get(reverse("tasks:task-detail", args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_detail.html")
        self.assertContains(response, self.task.name)

    def test_task_create_view(self):
        data = {
            "name": "New Task",
            "task_type": self.task_type.pk,
            "is_completed": False,
            "description": "New task description",
            "deadline": (now() + timedelta(days=10)).date(),
            "priority": 0,
            "assignees": self.user.pk
        }
        response = self.client.post(reverse("tasks:task-create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("tasks:task-list"))
        self.assertEqual(Task.objects.count(), 2)

    def test_task_delete_view(self):
        response = self.client.post(reverse("tasks:task-delete", args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_change_status_view(self):
        response = self.client.post(reverse("tasks:task-change-status", args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)

    def test_task_history_view(self):
        self.task.is_completed = True
        self.task.save()
        response = self.client.get(reverse("tasks:task-list-history"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)


class PositionViewsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.position = Position.objects.create(name="Tester")
        self.client.login(username="testuser", password="testpass")

    def test_position_list_view(self):
        position = Position.objects.create(name="Developer")
        response = self.client.get(reverse("tasks:position-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, position.name)

    def test_position_create_view(self):
        response = self.client.post(reverse("tasks:position-create"), {"name": "Designer"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Position.objects.count(), 2)

    def test_position_delete_view(self):
        response = self.client.post(reverse("tasks:position-delete", args=[self.position.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Position.objects.count(), 0)


class TaskTypeViewsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.task_type = TaskType.objects.create(name="QA")
        self.client.login(username="testuser", password="testpass")

    def test_task_type_list_view(self):
        task_type = TaskType.objects.create(name="Developer")
        response = self.client.get(reverse("tasks:task-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task_type.name)

    def test_task_type_create_view(self):
        response = self.client.post(reverse("tasks:task-type-create"), {"name": "Designer"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TaskType.objects.count(), 2)

    def test_task_type_delete_view(self):
        response = self.client.post(reverse("tasks:task-type-delete", args=[self.task_type.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TaskType.objects.count(), 0)
