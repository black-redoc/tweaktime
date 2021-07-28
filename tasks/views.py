from django.views.generic import ListView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm


class TasksListView(ListView):
    template_name = "pages/home.html"
    model = Task


class UnDoneTaskFormAndList(FormView, SuccessMessageMixin):
    template_name = "tasks/undone.html"
    form_class = TaskForm
    success_message = "Task created successful!"
    model = Task

    def get_success_url(self):
        return reverse_lazy("tasks:undone")

    def get_context_data(self, **kwargs):
        context = super(UnDoneTaskFormAndList, self).get_context_data(**kwargs)
        context.update({"undone_tasks": "tasks"})
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
