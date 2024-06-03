from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def ratings(request):
    return render(request, "ratings.html")


def problems(request):
    return render(request, "problems.html")


def contests(request):
    return render(request, "contests.html")


def profile(request):
    return render(request, "profile.html")
