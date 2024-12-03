from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import RegisterForm, LoginForm, WorkerUpdateForm
from accounts.models import Worker

User = get_user_model()
class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = RegisterForm
    template_name = "registration/register.html"


class WorkerListView(generic.ListView):
    model = get_user_model()


class WorkerDetailView(generic.DetailView):
    model = get_user_model()


class WorkerUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("accounts:worker-list")


class WorkerDeleteView(generic.DetailView):
    model = get_user_model()


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("accounts:login/")

        else:
            msg = 'Form is not valid'
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form, "msg": msg, "success": success})
