from django import forms
from django.contrib.auth import get_user_model

from tasks.models import Position, Task, TaskType


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Deadline",
    )


    class Meta:
        model = Task
        fields = [
            "name",
            "task_type",
            "is_completed",
            "description",
            "deadline",
            "priority",
            "assignees",
        ]


class TaskTypeForm(forms.ModelForm):
    name = forms.CharField(label=("Name"), required=True)

    class Meta:
        model = TaskType
        fields = ["name"]


class PositionForm(forms.ModelForm):
    name = forms.CharField(label=("Name"))

    class Meta:
        model = Position
        fields = ["name"]


