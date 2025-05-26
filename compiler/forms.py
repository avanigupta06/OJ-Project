from django import forms
from compiler.models import CodeSubmission

LANGUAGE_CHOICES = [
    ('python', 'Python'),
    ('cpp', 'C++'),
]


class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-select form-select-sm w-auto'}) )

    class Meta:
        model = CodeSubmission
        fields = ['language', 'code', 'input_data']
        widgets = {
            'code': forms.Textarea(attrs={
                'class': 'form-control',  # ⬅️ Bootstrap input style
                'rows': 14,
                'cols': 80,
                'placeholder': 'Write your code here...',
                'style': 'resize: vertical;'
            }),
            'input_data': forms.Textarea(attrs={
                'class': 'form-control',  # ⬅️ Bootstrap input style
                'rows': 3,
                'cols': 10,
                'placeholder': 'Enter custom input...',
                'style': 'resize: vertical;'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['input_data'].required = False 
