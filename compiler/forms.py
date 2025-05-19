from django import forms
from compiler.models import CodeSubmission

LANGUAGE_CHOICES = [
    ('python', 'Python'),
    ('cpp', 'C++'),
]


class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    class Meta:
        model = CodeSubmission
        fields = ["language", "code"]
