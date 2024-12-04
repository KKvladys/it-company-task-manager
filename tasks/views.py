from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from tasks.forms import TaskForm, PositionForm, TaskTypeForm
from tasks.models import Task, Position, TaskType


@login_required(login_url="accounts/login/")
def home(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    num_task_urgent = tasks.filter(priority="Urgent", is_completed=False).count()
    num_task_high = tasks.filter(priority="High", is_completed=False).count()
    num_task_medium = tasks.filter(priority="Medium", is_completed=False).count()
    num_task_low = tasks.filter(priority="Low", is_completed=False).count()
    context = {
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
    fields = "__all__"


class TaskDeliteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class PositionListView(generic.ListView):
    model = Position


class PositionCreateView(generic.CreateView):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy("tasks:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("tasks:position-list")


class PositionDetailView(generic.DetailView):
    model = Position


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = ["name"]


class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeUpdateView(generic.UpdateView):
    model = TaskType
    fields = ["name"]


class TaskTypeDeleteView(generic.DeleteView):
    model = TaskType


class TaskTypeDetailView(generic.DetailView):
    model = TaskType


def change_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse("tasks:task-list"))
