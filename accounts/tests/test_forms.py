from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import RegisterForm, LoginForm, WorkerUpdateForm
from tasks.models import Position

User = get_user_model()


class RegisterFormTests(TestCase):
    def test_valid_data(self):
        form = RegisterForm(data={
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "strongpassword",
            "password2": "strongpassword"
        })
        self.assertTrue(form.is_valid())

    def test_missing_email(self):
        form = RegisterForm(data={
            "username": "testuser",
            "password1": "strongpassword",
            "password2": "strongpassword"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_password_mismatch(self):
        form = RegisterForm(data={
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "pass1",
            "password2": "pass2"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


class LoginFormTests(TestCase):
    def test_valid_data(self):
        form = LoginForm(data={
            "username": "testuser",
            "password": "strongpassword"
        })
        self.assertTrue(form.is_valid())

    def test_missing_username(self):
        form = LoginForm(data={
            "password": "strongpassword"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_missing_password(self):
        form = LoginForm(data={
            "username": "testuser"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("password", form.errors)


class WorkerUpdateFormTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Software Engineer")
        self.worker = User.objects.create_user(
            username="testuser",
            password="strongpassword",
            first_name="Test",
            last_name="User",
            position=self.position
        )

    def test_valid_data(self):
        form = WorkerUpdateForm(data={
            "first_name": "Updated",
            "last_name": "Name",
            "position": self.position.id
        }, instance=self.worker)
        self.assertTrue(form.is_valid())

    def test_invalid_position(self):
        form = WorkerUpdateForm(data={
            "first_name": "Updated",
            "last_name": "Name",
            "position": 999
        }, instance=self.worker)
        self.assertFalse(form.is_valid())
        self.assertIn("position", form.errors)
