from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class TasksListView(ListView):
    template_name = "pages/home.html"
    model = Task


class UnDoneTaskFormAndList(FormView):
    template_name = "tasks/undone.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:undone")

    def get_context_data(self, **kwargs):
        context = kwargs.copy()
        context["undone_tasks"] = "tasks"
        return super().get_context_data(**context)
