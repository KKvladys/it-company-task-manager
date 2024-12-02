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
    template_name = "accounts/worker_list.html"


class WorkerDetailView(generic.DetailView):
    model = get_user_model()
    context_object_name = "worker_list"
    template_name = "accounts/worker_detail.html"