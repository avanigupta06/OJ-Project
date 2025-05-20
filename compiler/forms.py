from django import forms
from compiler.models import CodeSubmission

LANGUAGE_CHOICES = [
    ('python', 'Python'),
    ('cpp', 'C++'),
]


class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    code = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 20, 
            'cols': 85, 
            'style': 'font-family: monospace; height: 400px;', 
            'placeholder': 'Write your code here...'
        })
    )

    class Meta:
        model = CodeSubmission
        fields = ["language", "code"]
