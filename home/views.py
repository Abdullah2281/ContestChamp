from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
# from .forms import CustomUserCreationForm
from .models import UserProfile
from .models import CustomUser
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import CustomUser, Friendship

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


def logout_view(request):
    logout(request)
    return redirect("login")


def ratings(request):
    users = CustomUser.objects.all()
    current_user = {}
    if request.user.is_authenticated:
        user_ = request.user
        current_user["username"] = user_.username
        current_user["rating"] = user_.rating
        # print("User Exit")
    user_ratings = {}
    for user in users:
        # Example: Calculate rating based on user's activity or performance
        # Replace this with your actual rating calculation logic
        rating = user.rating
        user_ratings[user.username] = rating
    return render(
        request,
        "ratings.html",
        {"user_ratings": user_ratings, "Current_user": current_user},
    )


def problems(request):
    return render(request, "problems.html")


def contests(request):
    return render(request, "contests.html")

@login_required
def profile(request, user_id):
    requested_user = CustomUser.objects.filter(username=user_id)
    if not requested_user.exists():
        messages.error(request, "No such user exists")
        return redirect("home")
    
    requested_user = requested_user.first()
    current_user = request.user
    
    # Fetch friends of the requested user
    friends = Friendship.objects.filter(user=requested_user).values_list('friend', flat=True)
    friends_list = CustomUser.objects.filter(id__in=friends)
    
    user_data = {
        "username": requested_user.username,
        "rating": requested_user.rating,
        "first_name": requested_user.first_name,
        "university": requested_user.university,
        "is_current_user": current_user.username == user_id,
        "friends": friends_list
    }
    
    if current_user.username == user_id:
        user_data["email"] = requested_user.email
    
    return render(request, "profile.html", {"user": user_data})

@login_required
def add_friend(request, user_id):
    friend = get_object_or_404(CustomUser, username=user_id)
    current_user = request.user

    if friend == current_user:
        messages.error(request, "You cannot add yourself as a friend.")
        return redirect('profile', user_id=user_id)
    
    # Check if already friends
    existing_friendship = Friendship.objects.filter(user=current_user, friend=friend).exists()
    if existing_friendship:
        messages.info(request, "You are already friends.")
    else:
        # Create a new friendship
        Friendship.objects.create(user=current_user, friend=friend)
        messages.success(request, f"You are now friends with {friend.username}.")

    return redirect('profile', user_id=user_id)

def user_view(request):
    current_user = request.user
    if len(current_user.username) == 0:
        return redirect("login")
    url = str("profile/" + current_user.username)
    return redirect(url)


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["mail"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        university = request.POST["university"]
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
                    user.university = university
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

#profile settings
@login_required
def settings(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        university = request.POST["university"]
        curr_password = request.POST["password"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        user = request.user

        if not check_password(curr_password, user.password):
            messages.error(request, "Wrong Password")
            return redirect('settings')
        if password1 and password2 and password1 != password2:
            messages.error(request, "Passwords did not match.")
            return redirect('settings')
        
        if CustomUser.objects.filter(email=email).exists() and user.email != email:
            messages.error(request, "Email already exists")
            return redirect('settings')
        
        # Update user fields
        user.first_name = first_name
        user.email = email

        if password1:
            user.password = make_password(password1)
        user.save()

        # Update profile fields
        profile = CustomUser.objects.get(username = user.username)
        profile.university = university
        profile.save()

        messages.success(request, 'Your profile has been updated successfully.')
        url = str("profile/" + user.username)
        return redirect(url)
    else:
        return render(request, 'profile_settings.html')
    

def user_search(request):
    query = request.GET.get('q', '')
    if query:
        users = CustomUser.objects.filter(username__icontains=query)[:10]  # Limiting to 10 results
        results = [{'username': user.username} for user in users]
    else:
        results = []
    return JsonResponse(results, safe=False)