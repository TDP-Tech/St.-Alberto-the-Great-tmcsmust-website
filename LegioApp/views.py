from django.shortcuts import render, redirect, get_object_or_404
from .models import LegioMemberTransaction
from .forms import LegioMemberTransactionForm, LegioMemberTransactionFilterForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

def legio_page(request):
    return render(request, 'legio.html')

def legio_member_transaction_create(request):
    if request.method == 'POST':
        form = LegioMemberTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('legio-transaction-list')
    else:
        form = LegioMemberTransactionForm()
    return render(request, 'legio_member_transaction_create.html', {'form': form})

def legio_member_transaction_list(request):
    transactions = LegioMemberTransaction.objects.all().order_by('-id')
    filter_form = LegioMemberTransactionFilterForm(request.POST or None)
    
    if request.method == 'POST':
        if filter_form.is_valid():
            member_name = filter_form.cleaned_data.get('member_name')
            transaction_type = filter_form.cleaned_data.get('transaction_type')
            start_date = filter_form.cleaned_data.get('start_date')
            end_date = filter_form.cleaned_data.get('end_date')

            if member_name:
                transactions = transactions.filter(member__first_name__icontains=member_name) | \
                                transactions.filter(member__last_name__icontains=member_name)
            if transaction_type:
                transactions = transactions.filter(transaction_type=transaction_type)
            if start_date:
                transactions = transactions.filter(transaction_date__gte=start_date)
            if end_date:
                transactions = transactions.filter(transaction_date__lte=end_date)

    return render(request, 'legio_member_transaction_list.html', {'transactions': transactions, 'filter_form': filter_form})

def legio_member_transaction_update(request, pk):
    transaction = LegioMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = LegioMemberTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('legio-transaction-list')
    else:
        form = LegioMemberTransactionForm(instance=transaction)
    return render(request, 'legio_member_transaction_update.html', {'form': form})

def legio_member_transaction_delete(request, pk):
    transaction = LegioMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('legio-transaction-list')
    return render(request, 'legio_member_transaction_delete.html', {'transaction': transaction})

def legio_member_transaction_details(request, member_pk):
    transactions = LegioMemberTransaction.objects.filter(member_id=member_pk).order_by('-transaction_date')
    total_amount_paid = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    return render(request, 'legio_member_transaction_details.html', {'transactions': transactions,'total_amount_paid': total_amount_paid})

from .models import TmcsMember
def legio_member_list(request):
    legio_members = TmcsMember.objects.filter(vyama_vya_kitume__icontains='LEGIO MARIA')
    return render(request, 'legio_member_list.html', {'legio_members': legio_members})


@login_required
def individual_transactions(request):
    transactions = LegioMemberTransaction.objects.filter(member=request.user)
    context = { 'transactions': transactions}
    return render(request, 'individual_transactions.html', context)

