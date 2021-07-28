from tasks.forms import TaskForm
from django.test import TestCase


class TaskTests(TestCase):
    """
    Test storing of TaskForm
    """

    def test_task_form_storing(self):
        title_expected = "title1"
        task_str = "Task(pk=1, title=title1, status=undone)"

        form = TaskForm(
            data={
                "title": "title1",
                "description": "desc1",
                "priority": "moderate",
                "status": "undone",
            }
        )

        new_task = form.save()

        self.assertEqual(new_task.title, title_expected)
        self.assertEqual(new_task.__str__(), task_str)
