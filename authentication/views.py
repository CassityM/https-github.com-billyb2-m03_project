from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import AuthForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def register_page(request):
    if request.method == "GET":
        form = AuthForm
        return render(request, "register.html", {"form": form})

    else:
        form = AuthForm(request.POST)

        if not form.is_valid():
            return HttpResponse("Invalid form")

        username = form.cleaned_data["username"]

        # Check if the user is already registered
        if User.objects.filter(username=username).exists():
            return HttpResponse("User already registered")

        else:
            password = form.cleaned_data["password"]

            user = User(username=username)
            user.set_password(password)

            user.save()
            # Sets the user's auth cookie
            login(request, user)

            return HttpResponse(
                    "User: " + user.username +
                    " password: " + user.password
            )


def login_page(request):
    if request.method == "GET":
        form = AuthForm
        return render(request, "login.html", {"form": form})

    if request.method == "POST":
        form = AuthForm(request.POST)

        if not form.is_valid():
            return HttpResponse("Invalid form")

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(request, username=username, password=password)

        # Sucess
        if user is not None:
            login(request, user)
            return HttpResponse("Login sucess")

        else:
            return render(request, "invalid_login.html", {"form": form})


def view_item(request, item_id):
    if request.method == "GET":
        return HttpResponse("Viewing item %s" % item_id)

    else:
        data = request.POST["hi"]
        return HttpResponse("Hi? %s" % data)
