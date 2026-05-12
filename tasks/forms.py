from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "scheduled_at",
            "location",
            "caution",
            "preparation",
            "detail",
        ]
        widgets = {
            "scheduled_at": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={"type": "datetime-local"},
            ),
            "caution": forms.Textarea(attrs={"rows": 3}),
            "preparation": forms.Textarea(attrs={"rows": 3}),
            "detail": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = self.fields.get("scheduled_at")
        if field:
            field.input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M:%S"]

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("To do を入力してください。")
        return title