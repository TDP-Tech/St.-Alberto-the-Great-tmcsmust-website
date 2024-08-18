from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MemberTransaction
from .forms import MemberTransactionForm, TransactionFilterForm
from django.urls import reverse
from django.db.models import Sum
from django.contrib import messages
from AuthenticationApp.models import TmcsMember


@login_required
def member_transaction_create(request):
    if request.method == 'POST':
        form = MemberTransactionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['amount'] > 0:
                # Get the current user
                user = request.user
                # Check if the user is a mhazini_tawi
                if user.is_authenticated and user.is_mhazini_tawi:
                    # Save the transaction with created_by set to the current user
                    transaction = form.save(commit=False)
                    transaction.created_by = user
                    transaction.save()
                    return redirect('transaction-list')
                else:
                    messages.error(request, "You don't have permission to create transactions.")
            else:
                messages.error(request, "Amount should be greater than 0.")
        else:
            messages.error(request, "Form is invalid. Please check the input data.")
    else:
        form = MemberTransactionForm()
    return render(request, 'member_transaction_create.html', {'form': form})


# @login_required
# def member_transaction_create(request):
#     if request.method == 'POST':
#         form = MemberTransactionForm(request.POST)
#         if form.is_valid():
#             # Get the member and their level of study
#             member = form.cleaned_data['member']
#             level_of_study = member.level_of_study
            
#             # Get the transaction type and amount from the form
#             transaction_type = form.cleaned_data['transaction_type']
#             amount = form.cleaned_data['amount']
            
#             # Calculate the amount based on the level of study and transaction type
#             if level_of_study and transaction_type:
#                 if transaction_type == 'Ada':
#                     if level_of_study == 'Certificate':
#                         amount = 2000
#                     elif level_of_study == 'Diploma':
#                         amount = 2000 * 3
#                     elif level_of_study.startswith('Bachelor'):
#                         amount = 2000 * 4  # Bachelor's degree is 4 years
#                     elif level_of_study == 'Doctor of Philosophy':
#                         amount = 2000 * 2  # Align Doctor of Philosophy with Bachelor's degree with 4 years
#                 elif transaction_type == 'Zaka':
#                     if level_of_study == 'Certificate':
#                         amount = max(2000, amount)  # Minimum is 2000
#                     elif level_of_study == 'Diploma':
#                         amount = max(2000 * 3, amount)  # Minimum is 6000 for 3 years
#                     elif level_of_study.startswith('Bachelor'):
#                         amount = max(2000 * 4, amount)  # Minimum is 8000 for 4 years
#                     elif level_of_study == 'Doctor of Philosophy':
#                         amount = max(2000 * 2, amount)  # Align Doctor of Philosophy with Bachelor's degree with 4 years
#                 elif transaction_type == 'Tunisha mfuko':
#                     amount = 10000  # Fixed amount for all levels
#                 elif transaction_type == 'Sherehe na Maafa':
#                     if level_of_study == 'Diploma':
#                         amount = 6000
#                     elif level_of_study.startswith('Bachelor'):
#                         amount = 12000 if level_of_study.endswith('4 years') else 16000
#                     elif level_of_study == 'Doctor of Philosophy':
#                         amount = 12000 if level_of_study.endswith('2 years') else 16000  # Align Doctor of Philosophy with Bachelor's degree with 4 years
#                 elif transaction_type == 'Cheti':
#                     amount = 4000  # Fixed amount for all levels
            
#             # Check if the calculated amount is greater than 0
#             if amount > 0:
#                 # Get the current user
#                 user = request.user
#                 # Check if the user is a mhazini_tawi
#                 if user.is_authenticated and user.is_mhazini_tawi:
#                     # Save the transaction with created_by set to the current user
#                     transaction = form.save(commit=False)
#                     transaction.created_by = user
#                     transaction.amount = amount  # Set the calculated amount
#                     transaction.save()
#                     return redirect('transaction-list')
#                 else:
#                     messages.error(request, "You don't have permission to create transactions.")
#             else:
#                 messages.error(request, "Amount should be greater than 0.")
#         else:
#             messages.error(request, "Form is invalid. Please check the input data.")
#     else:
#         form = MemberTransactionForm()
#     return render(request, 'member_transaction_create.html', {'form': form})

def member_transaction_list(request):
    transactions = MemberTransaction.objects.all().order_by('-id')
    filter_form = TransactionFilterForm(request.POST or None)
    
    if request.method == 'POST':
        if filter_form.is_valid():
            member_name = filter_form.cleaned_data.get('member_name')
            transaction_type = filter_form.cleaned_data.get('transaction_type')
            start_date = filter_form.cleaned_data.get('start_date')
            end_date = filter_form.cleaned_data.get('end_date')

            # Filter by member name if provided
            if member_name:
                # Split the member name into first, middle, and last name
                names = member_name.split()

                # Filter by first, middle, and last name if provided
                for name in names:
                    transactions = transactions.filter(
                        member__first_name__icontains=name) | \
                                    transactions.filter(
                        member__middle_name__icontains=name) | \
                                    transactions.filter(
                        member__last_name__icontains=name)

            # Optionally filter by transaction type
            if transaction_type:
                transactions = transactions.filter(transaction_type=transaction_type)

            # Optionally filter by start date
            if start_date:
                transactions = transactions.filter(transaction_date__gte=start_date)

            # Optionally filter by end date
            if end_date:
                transactions = transactions.filter(transaction_date__lte=end_date)

    return render(request, 'member_transaction_list.html', {'transactions': transactions, 'filter_form': filter_form})

def member_transaction_update(request, pk):
    transaction = MemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = MemberTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction-list')
    else:
        form = MemberTransactionForm(instance=transaction)
    return render(request, 'member_transaction_update.html', {'form': form})

def member_transaction_delete(request, pk):
    transaction = MemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction-list')
    return render(request, 'member_transaction_delete.html', {'transaction': transaction})

# def individual_member_transaction_details(request, member_id):
#     transactions = MemberTransaction.objects.filter(member_id=member_id).order_by('-transaction_date')
#     total_amount_paid = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
#     # Retrieve member details
#     member = TmcsMember.objects.get(pk=member_id)
#     member_id = member.generate_member_id()
#     return render(request, 'individual_member_transaction_details.html', {'transactions': transactions, 'total_amount_paid': total_amount_paid, 'member_id':member_id})

from django.contrib.auth.decorators import login_required

@login_required
def individual_member_transaction_details(request, member_id):
    transactions = MemberTransaction.objects.filter(member_id=member_id).order_by('-transaction_date')
    total_amount_paid = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    
    # Retrieve member details
    member = TmcsMember.objects.get(pk=member_id)
    member_id = member.generate_member_id()

    # Check if the current user is authorized to print receipts
    mhazini_name = ""
    if request.user.is_authenticated and request.user.is_mhazini_tawi:
        mhazini_name = f"{request.user.first_name} {request.user.last_name}"

    return render(request, 'individual_member_transaction_details.html', {'transactions': transactions, 'total_amount_paid': total_amount_paid, 'member_id': member_id, 'mhazini_name': mhazini_name})



@login_required
def individual_transactions(request):
    transactions = MemberTransaction.objects.filter(member=request.user)
    context = { 'transactions': transactions}
    return render(request, 'individual_transactions.html', context)

