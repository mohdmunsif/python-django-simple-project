from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import render, redirect

from users.forms import SignUpForm
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)


def login_view(request):
    if request.method == 'GET':
        return render(request, "users/user.html", context)
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("entries:browse"))
        else:
            return render(request, "users/login.html", {"message": "Invalid credentials."})


def account_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("entries:browse"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})


def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("entries:browse"))
        else:
            return render(request, "users/signup.html", {"form": form})

    else:
        form = SignUpForm()
        return render(request, "users/signup.html", {"form": form})
    # return render(request, "users/signup.html", {"message": "Invalid credentials."})
