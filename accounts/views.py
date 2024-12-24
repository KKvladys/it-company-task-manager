from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView

from accounts.forms import RegisterForm, LoginForm, WorkerUpdateForm, PositionForm
from accounts.models import Position

User = get_user_model()


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        solved_tasks_count = user.tasks.filter(is_completed=True).count()
        context["solved_tasks_count"] = solved_tasks_count
        return context


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("accounts:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()


class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid credentials")
            return self.form_invalid(form)


class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        return super().form_valid(form)


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("accounts:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("accounts:position-list")


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = ["name"]
