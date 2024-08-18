from django import forms
from .models import MoyomtakatifuwaYesuMemberTransaction, TRANSACTION_CHOICES
from AuthenticationApp.models import TmcsMember

class MoyomtakatifuwaYesuMemberTransactionForm(forms.ModelForm):
    class Meta:
        model = MoyomtakatifuwaYesuMemberTransaction
        fields = ['member', 'transaction_type', 'amount']
        labels = {
            'member': 'Member Unique Identifier',
            'transaction_type': 'Transaction Type',
            'amount': 'Amount',
        }
        widgets = {
            'member': forms.Select(attrs={'class': 'form-control col-md-5'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control col-md-5'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control col-md-5'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter members who are part of the MOYO MTAKATIFU WA YESU group
        self.fields['member'].queryset = TmcsMember.objects.filter(vyama_vya_kitume='MOYO MTAKATIFU WA YESU')

class MoyomtakatifuwaYesuMemberTransactionFilterForm(forms.Form):
    member_name = forms.CharField(label='Member Name', required=False)
    transaction_type = forms.ChoiceField(label='Transaction Type', required=False, choices=TRANSACTION_CHOICES)
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
