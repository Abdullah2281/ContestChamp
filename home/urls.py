from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.my_login_view, name="login"),
    path("ratings", views.ratings, name="ratings"),
    path("problems", views.problems, name="problems"),
    path("contests", views.contests, name="contests"),
    path("profile", views.profile, name="profile"),
    path("register", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
]
