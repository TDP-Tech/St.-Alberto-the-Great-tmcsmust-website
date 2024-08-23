from django.shortcuts import render, redirect, get_object_or_404
from .models import KarismatikiMemberTransaction
from .forms import KarismatikiMemberTransactionForm, KarismatikiMemberTransactionFilterForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

def karismatiki_page(request):
    return render(request, 'karismatiki.html')

def karismatiki_member_transaction_create(request):
    if request.method == 'POST':
        form = KarismatikiMemberTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('karismatiki-transaction-list')
    else:
        form = KarismatikiMemberTransactionForm()
    return render(request, 'karismatiki_member_transaction_create.html', {'form': form})

def karismatiki_member_transaction_list(request):
    transactions = KarismatikiMemberTransaction.objects.all().order_by('-id')
    filter_form = KarismatikiMemberTransactionFilterForm(request.POST or None)
    
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

    return render(request, 'karismatiki_member_transaction_list.html', {'transactions': transactions, 'filter_form': filter_form})

def karismatiki_member_transaction_update(request, pk):
    transaction = KarismatikiMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = KarismatikiMemberTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('karismatiki-transaction-list')
    else:
        form = KarismatikiMemberTransactionForm(instance=transaction)
    return render(request, 'karismatiki_member_transaction_update.html', {'form': form})

def karismatiki_member_transaction_delete(request, pk):
    transaction = KarismatikiMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('karismatiki-transaction-list')
    return render(request, 'karismatiki_member_transaction_delete.html', {'transaction': transaction})

def karismatiki_member_transaction_details(request, member_pk):
    transactions = KarismatikiMemberTransaction.objects.filter(member_id=member_pk).order_by('-transaction_date')
    total_amount_paid = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    return render(request, 'karismatiki_member_transaction_details.html', {'transactions': transactions,'total_amount_paid': total_amount_paid})

from .models import TmcsMember
def karismatiki_member_list(request):
    karismatiki_members = TmcsMember.objects.filter(vyama_vya_kitume__icontains='KARISMATIKI')
    return render(request, 'karismatiki_member_list.html', {'karismatiki_members': karismatiki_members})



@login_required
def individual_transactions(request):
    transactions = KarismatikiMemberTransaction.objects.filter(member=request.user)
    context = { 'transactions': transactions}
    return render(request, 'individual_transactions.html', context)

