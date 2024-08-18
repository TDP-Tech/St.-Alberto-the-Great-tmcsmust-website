from django import forms
from .models import Mauzo, MauzoDeletionLog, Matumizi, MatumiziDeletionLog, MauzoEditedLog, MatumiziEditedLog

class MauzoForm(forms.ModelForm):
    class Meta:
        model = Mauzo
        fields = ['date', 'mauzo_tshirt', 'mauzo_visakramenti', 'mauzo_vipeperushi', 'mapato_saloon']
        labels = {
            'date': 'Date',
            'mauzo_tshirt': 'Mauzo Tshirt',
            'mauzo_visakramenti': 'Mauzo Visakramenti',
            'mauzo_vipeperushi': 'Mauzo Vipeperushi',
            'mapato_saloon': 'Mapato Saloon',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mauzo_tshirt': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_visakramenti': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_vipeperushi': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mapato_saloon': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }

class MauzoDeletionLogForm(forms.ModelForm):
    class Meta:
        model = MauzoDeletionLog
        fields = ['deleted_by', 'date', 'mauzo_tshirt', 'mauzo_visakramenti', 'mauzo_vipeperushi', 'mapato_saloon','reason']
        labels = {
            'deleted_by': 'Deleted By',
            'date': 'Date',
            'mauzo_tshirt': 'Mauzo Tshirt',
            'mauzo_visakramenti': 'Mauzo Visakramenti',
            'mauzo_vipeperushi': 'Mauzo Vipeperushi',
            'mapato_saloon': 'Mapato Saloon',
            'reason': 'Reason to delete this information',
        }
        widgets = {
            'deleted_by': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mauzo_tshirt': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_visakramenti': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_vipeperushi': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mapato_saloon': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }

class MauzoEditedLogForm(forms.ModelForm):
    class Meta:
        model = MauzoEditedLog
        fields = ['edited_by', 'mauzo', 'mauzo_tshirt_before', 'mauzo_visakramenti_before', 'mauzo_vipeperushi_before', 'mapato_saloon_before', 'mauzo_tshirt_after', 'mauzo_visakramenti_after', 'mauzo_vipeperushi_after', 'mapato_saloon_after']
        labels = {
            'edited_by': 'Edited By',
            'mauzo': 'Mauzo',
            'mauzo_tshirt_before': 'Mauzo Tshirt Before',
            'mauzo_visakramenti_before': 'Mauzo Visakramenti Before',
            'mauzo_vipeperushi_before': 'Mauzo Vipeperushi Before',
            'mapato_saloon_before': 'Mapato Saloon Before',
            'mauzo_tshirt_after': 'Mauzo Tshirt After',
            'mauzo_visakramenti_after': 'Mauzo Visakramenti After',
            'mauzo_vipeperushi_after': 'Mauzo Vipeperushi After',
            'mapato_saloon_after': 'Mapato Saloon After',
        }
        widgets = {
            'edited_by': forms.Select(attrs={'class': 'form-control'}),
            'mauzo': forms.Select(attrs={'class': 'form-control'}),
            'mauzo_tshirt_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_visakramenti_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_vipeperushi_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mapato_saloon_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_tshirt_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_visakramenti_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mauzo_vipeperushi_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'mapato_saloon_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }


class MatumiziForm(forms.ModelForm):
    class Meta:
        model = Matumizi
        fields = ['date', 'matumizi_tshirt', 'matumizi_visakramenti', 'matumizi_vipeperushi', 'matumizi_saloon']
        labels = {
            'date': 'Date',
            'matumizi_tshirt': 'Matumizi Tshirt',
            'matumizi_visakramenti': 'Matumizi Visakramenti',
            'matumizi_vipeperushi': 'Matumizi Vipeperushi',
            'matumizi_saloon': 'Matumizi Saloon',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'matumizi_tshirt': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_visakramenti': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_vipeperushi': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_saloon': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }

class MatumiziDeletionLogForm(forms.ModelForm):
    class Meta:
        model = MatumiziDeletionLog
        fields = ['deleted_by', 'date', 'matumizi_tshirt', 'matumizi_visakramenti', 'matumizi_vipeperushi', 'matumizi_saloon','reason']
        labels = {
            'deleted_by': 'Deleted By',
            'date': 'Date',
            'matumizi_tshirt': 'Matumizi Tshirt',
            'matumizi_visakramenti': 'Matumizi Visakramenti',
            'matumizi_vipeperushi': 'Matumizi Vipeperushi',
            'matumizi_saloon': 'Matumizi Saloon',
            'reason': 'Reason to delete this information',
        }
        widgets = {
            'deleted_by': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'matumizi_tshirt': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_visakramenti': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_vipeperushi': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_saloon': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }
        

class MatumiziEditedLogForm(forms.ModelForm):
    class Meta:
        model = MatumiziEditedLog
        fields = ['edited_by', 'matumizi', 'matumizi_tshirt_before', 'matumizi_visakramenti_before', 'matumizi_vipeperushi_before', 'matumizi_saloon_before', 'matumizi_tshirt_after', 'matumizi_visakramenti_after', 'matumizi_vipeperushi_after', 'matumizi_saloon_after']
        labels = {
            'edited_by': 'Edited By',
            'matumizi': 'Matumizi',
            'matumizi_tshirt_before': 'Matumizi Tshirt Before',
            'matumizi_visakramenti_before': 'Matumizi Visakramenti Before',
            'matumizi_vipeperushi_before': 'Matumizi Vipeperushi Before',
            'matumizi_saloon_before': 'Matumizi Saloon Before',
            'matumizi_tshirt_after': 'Matumizi Tshirt After',
            'matumizi_visakramenti_after': 'Matumizi Visakramenti After',
            'matumizi_vipeperushi_after': 'Matumizi Vipeperushi After',
            'matumizi_saloon_after': 'Matumizi Saloon After',
        }
        widgets = {
            'edited_by': forms.Select(attrs={'class': 'form-control'}),
            'matumizi': forms.Select(attrs={'class': 'form-control'}),
            'matumizi_tshirt_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_visakramenti_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_vipeperushi_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_saloon_before': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_tshirt_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_visakramenti_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_vipeperushi_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'matumizi_saloon_after': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }
        
