from django.shortcuts import render, redirect, get_object_or_404
from .models import MoyomtakatifuwaYesuMemberTransaction
from .forms import MoyomtakatifuwaYesuMemberTransactionForm, MoyomtakatifuwaYesuMemberTransactionFilterForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from AuthenticationApp.models import TmcsMember

def moyomtakatifuwaYesu_page(request):
    return render(request, 'moyomtakatifuwaYesu.html')

def moyomtakatifuwaYesu_member_transaction_create(request):
    if request.method == 'POST':
        form = MoyomtakatifuwaYesuMemberTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moyomtakatifuwaYesu-transaction-list')
    else:
        form = MoyomtakatifuwaYesuMemberTransactionForm()
    return render(request, 'moyomtakatifuwaYesu_member_transaction_create.html', {'form': form})

def moyomtakatifuwaYesu_member_transaction_list(request):
    transactions = MoyomtakatifuwaYesuMemberTransaction.objects.all().order_by('-id')
    filter_form = MoyomtakatifuwaYesuMemberTransactionFilterForm(request.POST or None)
    
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

    return render(request, 'moyomtakatifuwaYesu_member_transaction_list.html', {'transactions': transactions, 'filter_form': filter_form})

def moyomtakatifuwaYesu_member_transaction_update(request, pk):
    transaction = MoyomtakatifuwaYesuMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = MoyomtakatifuwaYesuMemberTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('moyomtakatifuwaYesu-transaction-list')
    else:
        form = MoyomtakatifuwaYesuMemberTransactionForm(instance=transaction)
    return render(request, 'moyomtakatifuwaYesu_member_transaction_update.html', {'form': form})

def moyomtakatifuwaYesu_member_transaction_delete(request, pk):
    transaction = MoyomtakatifuwaYesuMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('moyomtakatifuwaYesu-transaction-list')
    return render(request, 'moyomtakatifuwaYesu_member_transaction_delete.html', {'transaction': transaction})

def moyomtakatifuwaYesu_member_transaction_details(request, member_pk):
    transactions = MoyomtakatifuwaYesuMemberTransaction.objects.filter(member_id=member_pk).order_by('-transaction_date')
    total_amount_paid = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    return render(request, 'moyomtakatifuwaYesu_member_transaction_details.html', {'transactions': transactions,'total_amount_paid': total_amount_paid})


def moyomtakatifuwaYesu_member_list(request):
    moyomtakatifuwaYesu_members = TmcsMember.objects.filter(vyama_vya_kitume__icontains='MOYO MTAKATIFU WA YESU')
    return render(request, 'moyomtakatifuwaYesu_member_list.html', {'moyomtakatifuwaYesu_members': moyomtakatifuwaYesu_members})



@login_required
def individual_transactions(request):
    transactions = MoyomtakatifuwaYesuMemberTransaction.objects.filter(member=request.user)
    context = { 'transactions': transactions}
    return render(request, 'individual_transactions.html', context)

