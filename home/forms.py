from django import forms
from home.models import Problem
from home.models import HiddenTestCase



class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description', 'difficulty', 'input_testcase', 'output_testcase']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10,'cols': 70}),
            'input_testcase': forms.Textarea(attrs={'rows': 3}),
            'output_testcase': forms.Textarea(attrs={'rows': 3}),
        }

class HiddenTestCaseForm(forms.ModelForm):
    class Meta:
        model = HiddenTestCase
        fields = ['problem', 'input_data', 'expected_output']
        widgets = {
            'problem': forms.Select(attrs={'class': 'form-select'}),
            'input_data': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'expected_output': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }