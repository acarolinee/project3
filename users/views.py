from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    # return render(request, "users/user.html", context)
    return render(request, "orders/order.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def registrate_view(request):
    if request.method == 'GET':
        return render(request, "users/registrate.html")
    elif request.method == 'POST':
        print ("llegue")
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, email=None, password=password)
        except IntegrityError:
            return render(request, "users/registrate.html", {"message": "User already exists"})

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/registrate.html", {"message": "Invalid registration"})
