from django.urls import path
from .views import TasksListView

app_name = "tasks"

urlpatterns = [
    path("timer", TasksListView.as_view(), name="timer"),
]
