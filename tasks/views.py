from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from tasks.forms import TaskForm, TaskTypeForm, TaskSearchForm
from tasks.models import Task, TaskType


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "tasks/home.html"
    login_url = "accounts/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context["num_task_urgent"] = tasks.filter(
            priority="0", is_completed=False
        ).count()
        context["num_task_high"] = tasks.filter(
            priority="1", is_completed=False
        ).count()
        context["num_task_medium"] = tasks.filter(
            priority="2", is_completed=False
        ).count()
        context["num_task_low"] = tasks.filter(priority="3", is_completed=False).count()
        return context


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = (
            Task.objects.filter(is_completed=False)
            .select_related("task_type")
            .prefetch_related("assignees")
        )

        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class TaskHistoryListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    context_object_name = "task_history_list"
    queryset = Task.objects.filter(is_completed=True)
    template_name = "tasks/task_history_list.html"


class TaskDtailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "tasks/task_type_list.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = "tasks/task_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    context_object_name = "task_type"
    template_name = "tasks/task_type_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType


class ChangeTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect(reverse("tasks:task-list"))
