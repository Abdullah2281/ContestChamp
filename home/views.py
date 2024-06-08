from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import UserProfile
from .models import CustomUser
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, "home.html")


def my_login_view(request):
    if request.method == "POST":
        # Assuming you have username and password fields in your login form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect("home")
        else:
            # Handle authentication failure
            messages.error(request, "Invalid username or password")

    # If GET request or authentication failed, render the login page
    return render(request, "login.html")


def ratings(request):
    users = CustomUser.objects.all()
    user_ratings = {}
    for user in users:
        # Example: Calculate rating based on user's activity or performance
        # Replace this with your actual rating calculation logic
        rating = user.rating
        user_ratings[user.username] = rating
    return render(request, "ratings.html", {"user_ratings": user_ratings})


def problems(request):
    return render(request, "problems.html")


def contests(request):
    return render(request, "contests.html")


def profile(request):
    return render(request, "profile.html")


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         Name = request.POST["name"]
#         email = request.POST["mail"]
#         p1 = request.POST["password1"]
#         p2 = request.POST["password2"]
#         if p1 == p2:
#             user_1 = UserProfile
#             user_2 = CustomUser
#             user_2.username=username
#             user_2.name = Name
#             user_2.email = email
#             user_2.password = p1
#             user_1.user = user_2
#             UserProfile.objects.create(user=user_1)
#             messages.info(request, "User Created")

#             return redirect("login")
#         else:
#             messages.info(request, "Password Didn't match")
#             return redirect("register")
#     return render(request, "register.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["mail"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        rating = 0  # Get the rating from the form

        if password1 == password2:
            if not CustomUser.objects.filter(username=username).exists():
                if not CustomUser.objects.filter(email=email).exists():
                    user = CustomUser.objects.create_user(
                        username=username, password=password1, email=email
                    )
                    user.first_name = (
                        name  # Assuming 'name' field corresponds to first name
                    )
                    user.rating = rating  # Set the rating
                    user.save()
                    UserProfile.objects.create(user=user)
                    messages.success(request, "User Created")
                    return redirect("login")
                else:
                    messages.error(request, "Email already exists")
            else:
                messages.error(request, "Username already exists")
        else:
            messages.error(request, "Passwords didn't match")

    return render(request, "register.html")
