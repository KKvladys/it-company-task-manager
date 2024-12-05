from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task, Position, TaskType
from datetime import timedelta
from django.utils.timezone import now


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
            priority="High"
        )

        self.client.login(username='testuser', password='password123')

    def test_home_view(self):
        response = self.client.get(reverse("tasks:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/home.html")

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
            'name': 'New Task',
            'task_type': self.task_type.pk,
            'is_completed': False,
            'description': 'New task description',
            'deadline': (now() + timedelta(days=10)).date(),
            'priority': 'Low',
            "assignees": self.user.pk
        }
        response = self.client.post(reverse("tasks:task-create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("tasks:task-list"))


    def test_task_delete_view(self):
        response = self.client.post(reverse("tasks:task-delete", args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_history_view(self):
        self.task.is_completed = True
        self.task.save()
        response = self.client.get(reverse("tasks:task-list-history"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)


    def test_position_list_view(self):
        position = Position.objects.create(name="Developer")
        response = self.client.get(reverse("tasks:position-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, position.name)

    def test_task_type_list_view(self):
        response = self.client.get(reverse("tasks:task-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task_type.name)

