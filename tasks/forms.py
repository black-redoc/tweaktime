from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field, Div
from crispy_forms.bootstrap import FormActions, InlineField

from .models import Task
from .task_priority import task_priority
from .task_status import status_choice


class PrioritySelect(forms.Select):
    template_name = "tasks/select_priority.html"

    def __init__(self, attrs=None, choices=(), disabled_choices=()):
        super(PrioritySelect, self).__init__(attrs, choices=choices)
        self.disabled_choices = disabled_choices


class StatusSelect(forms.Select):
    template_name = "tasks/select_status.html"

    def __init__(self, attrs=None, choices=(), disabled_choices=()):
        super(StatusSelect, self).__init__(attrs, choices=choices)
        self.disabled_choices = disabled_choices


class TaskForm(forms.Form):
    title = forms.CharField(label="")
    description = forms.CharField(label="")
    priority = forms.ChoiceField(
        choices=task_priority, label="", widget=PrioritySelect()
    )
    status = forms.ChoiceField(
        choices=status_choice,
        label="",
        widget=StatusSelect(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = TaskFormHelper()


class TaskFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = "post"
        self.layout = Layout(
            Div(
                Field("title", placeholder="title"),
                Field("description", placeholder="description"),
                Field("priority"),
                Field("status"),
                FormActions(Submit("Save", "Save", css_class="btn btn-dark ml-2")),
                css_class="input-group mb-3",
            ),
        )
        self.render_required_fields = True
