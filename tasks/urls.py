from django.urls import path
from .views import TasksListView, UnDoneTaskFormAndList

app_name = "tasks"

urlpatterns = [
    path("timer", TasksListView.as_view(), name="timer"),
    path("undone", UnDoneTaskFormAndList.as_view(), name="undone"),
]
