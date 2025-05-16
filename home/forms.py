from django import forms
from home.models import Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description', 'difficulty', 'input_testcase', 'output_testcase']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'input_testcase': forms.Textarea(attrs={'rows': 3}),
            'output_testcase': forms.Textarea(attrs={'rows': 3}),
        }
