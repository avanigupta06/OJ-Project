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
        fields = ['language', 'code', 'input_data']
        widgets = {
            'code': forms.Textarea(attrs={'rows': 15, 'cols': 80}),
            'input_data': forms.Textarea(attrs={'rows': 3, 'cols': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['input_data'].required = False  # ✅
