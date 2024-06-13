from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.my_login_view, name="login"),
    path("ratings", views.ratings, name="ratings"),
    path("problems", views.problems, name="problems"),
    path("contests", views.contests, name="contests"),
    path("profile/<str:user_id>", views.profile, name="profile"),
    path("register", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("profile", views.user_view, name="empty_user"),
    path("settings", views.settings, name="settings"),
]
