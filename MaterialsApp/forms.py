from django import forms
from .models import StudyMaterial

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['title', 'level','course', 'date_posted', 'document', 'year_of_study']  # Add 'year_of_study' field here if needed
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Example of title it can be something like Past papers for Communication Skills'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'date_posted': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'document': forms.FileInput(attrs={'class': 'form-control-file'}),
            'year_of_study': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'level': 'Level',
            'course': 'Course',
            'date_posted': 'Date Posted',
            'document': 'Document',
            'year_of_study': 'Year of Study',  # Modify label as needed
        }
