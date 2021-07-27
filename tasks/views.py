from django.views.generic import ListView
from .models import Task


class TasksListView(ListView):
    template_name = "pages/home.html"
    model = Task

class UnDoneTaskList(ListView):
    template_name = "tasks/undone.html"
    model = Task

