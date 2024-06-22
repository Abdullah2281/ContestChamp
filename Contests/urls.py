from django.urls import path
from . import views

urlpatterns = [
    path("contest/<int:contest_id>/problem/<str:code>/", views.problem, name="problem"),
    path("contests", views.contests, name="contests"),
    path("contests/<int:contest_id>", views.contests_show, name="contests_show"),
    path("contest/<int:contest_id>", views.contest_detail, name="contest"),
]
