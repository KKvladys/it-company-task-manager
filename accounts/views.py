from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic

from accounts.forms import RegisterForm
from accounts.models import Worker


# class WorkerCreateView(generic.CreateView):
#     model = Worker
#     form_class = RegisterForm
#     template_name = "registration/register.html"
#

class WorkerListView(generic.ListView):
    model = get_user_model()


class WorkerDetailView(generic.DetailView):
    model = get_user_model()


class WorkerUpdateView(generic.UpdateView):
    model = get_user_model()


class WorkerDeleteView(generic.DetailView):
    model = get_user_model()
