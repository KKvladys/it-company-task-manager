from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import TaskType, Position, Task
from datetime import datetime, timedelta

User = get_user_model()


class TaskTypeModelTests(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Development")

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Development")


class PositionModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Software Engineer")

    def test_position_str(self):
        self.assertEqual(str(self.position), "Software Engineer")


class TaskModelTests(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Bug Fixing")
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

        self.task = Task.objects.create(
            name="Fix login issue",
            description="Users cannot log in due to a server error.",
            deadline=datetime.now() + timedelta(days=7),
            is_completed=False,
            priority="High",
            task_type=self.task_type
        )
        self.task.assignees.set([self.user1, self.user2])

    def test_task_str(self):
        self.assertEqual(str(self.task), "Fix login issue")

    def test_task_fields(self):
        self.assertEqual(self.task.name, "Fix login issue")
        self.assertEqual(self.task.description, "Users cannot log in due to a server error.")
        self.assertEqual(self.task.is_completed, False)
        self.assertEqual(self.task.priority, "High")
        self.assertEqual(self.task.task_type, self.task_type)

    def test_task_assignees(self):
        self.assertIn(self.user1, self.task.assignees.all())
        self.assertIn(self.user2, self.task.assignees.all())
        self.assertEqual(self.task.assignees.count(), 2)

    def test_task_deadline(self):
        self.assertTrue(self.task.deadline > datetime.now())
