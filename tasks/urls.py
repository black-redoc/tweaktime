from django.urls import path
from .views import TasksListView, UnDoneTaskList

app_name = "tasks"

urlpatterns = [
    path("timer", TasksListView.as_view(), name="timer"),
    path("undone", UnDoneTaskList.as_view(), name="undone"),
]
