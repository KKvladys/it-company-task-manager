from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm, PositionForm, TaskTypeForm
from tasks.models import Task, Position, TaskType


@login_required(login_url="accounts/login/")
def home(request: HttpRequest) -> HttpResponse:
    num_task = Task.objects.count()
    num_task_urgent = Task.objects.filter(priority="Urgent").count()
    num_task_high = Task.objects.filter(priority="High").count()
    num_task_medium = Task.objects.filter(priority="Medium").count()
    num_task_low = Task.objects.filter(priority="Low").count()
    context = {
        "num_task": num_task,
        "num_task_urgent": num_task_urgent,
        "num_task_high": num_task_high,
        "num_task_medium": num_task_medium,
        "num_task_low": num_task_low
    }
    return render(request, "tasks/home.html", context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    queryset = Task.objects.filter(is_completed=False).prefetch_related("assignees")


class TaskHistoryListView(generic.ListView):
    model = Task
    paginate_by = 10
    context_object_name = "task_history_list"
    queryset = Task.objects.filter(is_completed=True)
    template_name = "tasks/task_history_list.html"


class TaskDtailView(generic.DetailView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task


class TaskDeliteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class PositionCreateView(generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("tasks:position-list")

class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:position-list")

class PositionListView(generic.ListView):
    model = Position


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")

class TaskTypeListView(generic.ListView):
    model = TaskType

    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"