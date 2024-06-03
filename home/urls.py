from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("ratings", views.ratings, name="ratings"),
    path("problems", views.problems, name="problems"),
    path("contests", views.contests, name="contests"),
    path("profile", views.profile, name="profile"),
]