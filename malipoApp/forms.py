from django import forms
from .models import MemberTransaction, TRANSACTION_CHOICES

class MemberTransactionForm(forms.ModelForm):
    class Meta:
        model = MemberTransaction
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


class TransactionFilterForm(forms.Form):
    member_name = forms.CharField(label='Member Name', required=False)
    transaction_type = forms.ChoiceField(label='Transaction Type', required=False, choices=TRANSACTION_CHOICES)
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
