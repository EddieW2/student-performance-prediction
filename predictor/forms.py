from django import forms
from .models import StudentPrediction


class StudentPredictionForm(forms.ModelForm):
    class Meta:
        model = StudentPrediction
        fields = [
            'name',
            'age',
            'attendance',
            'study_time',
            'previous_grade',
            'assignment_score',
            'participation',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter student name'
            }),

            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age',
                'min': 1
            }),

            'attendance': forms.NumberInput(attrs={
                'placeholder': 'e.g. 85',
                'min': 0,
                'max': 100,
                'step': 0.1
            }),

            'study_time': forms.NumberInput(attrs={
                'placeholder': 'Hours per week',
                'min': 0,
                'step': 0.1
            }),

            'previous_grade': forms.NumberInput(attrs={
                'placeholder': 'e.g. 70',
                'min': 0,
                'max': 100,
                'step': 0.1
            }),

            'assignment_score': forms.NumberInput(attrs={
                'placeholder': 'e.g. 75',
                'min': 0,
                'max': 100,
                'step': 0.1
            }),

            'participation': forms.NumberInput(attrs={
                'placeholder': 'e.g. 80',
                'min': 0,
                'max': 100,
                'step': 0.1
            }),
        }