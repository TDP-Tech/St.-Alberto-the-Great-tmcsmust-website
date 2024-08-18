# In forms.py inside your SadakaApp directory

from django import forms
from .models import Sadaka

class SadakaForm(forms.ModelForm):
    class Meta:
        model = Sadaka
        fields = ['date', 'sadaka1', 'shukrani']
        labels = {
            'date': 'Date',
            'sadaka1': 'Sadaka 1',
            'shukrani': 'Shukrani',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'sadaka1': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'shukrani': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }