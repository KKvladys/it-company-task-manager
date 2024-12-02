from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tasks.models import Task


def index(request: HttpRequest) -> HttpResponse:
    num_task = Task.objects.count()
    num_task_urgent = Task.objects.filter(priority="Urgent")
    num_task_high = Task.objects.filter(priority="High")
    num_task_medium = Task.objects.filter(priority="Medium")
    num_task_low = Task.objects.filter(priority="Low")
    context= {
        "num_task": num_task,
        "num_task_urgent": num_task_urgent,
        "num_task_high": num_task_high,
        "num_task_medium": num_task_medium,
        "num_task_low": num_task_low
    }
    return render(request, "tasks/index.html", context)