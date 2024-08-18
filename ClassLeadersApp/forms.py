from django import forms
from .models import ViongoziWaMadarasa

class ViongoziWaMadarasaForm(forms.ModelForm):
    class Meta:
        model = ViongoziWaMadarasa
        fields = ['user']
        labels = {
            'user': 'Select Member',
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

