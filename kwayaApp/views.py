from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, KwayaMemberTransaction, Achievement
from .forms import KwayaMemberTransactionForm, KwayaMemberTransactionFilterForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .forms import KwayaMemberTransactionForm, KwayaVoiceAssignment, KwayaVoiceAssignmentForm
from AuthenticationApp.models import TmcsMember

def kwaya_page(request):
    videos = Video.objects.all().order_by('-id')[:12]
    latest_video = Video.objects.order_by('-id').first()
    return render(request, 'kwaya.html', {'videos': videos, 'latest_video': latest_video})

def kwaya_member_transaction_create(request):
    if request.method == 'POST':
        form = KwayaMemberTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kwaya-transaction-list')
    else:
        form = KwayaMemberTransactionForm()
    return render(request, 'kwaya_member_transaction_create.html', {'form': form})

def kwaya_member_transaction_list(request):
    transactions = KwayaMemberTransaction.objects.all().order_by('-id')
    filter_form = KwayaMemberTransactionFilterForm(request.POST or None)
    
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

    return render(request, 'kwaya_member_transaction_list.html', {'transactions': transactions, 'filter_form': filter_form})

def kwaya_member_transaction_update(request, pk):
    transaction = KwayaMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = KwayaMemberTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('kwaya-transaction-list')
    else:
        form = KwayaMemberTransactionForm(instance=transaction)
    return render(request, 'kwaya_member_transaction_update.html', {'form': form})

def kwaya_member_transaction_delete(request, pk):
    transaction = KwayaMemberTransaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('kwaya-transaction-list')
    return render(request, 'kwaya_member_transaction_delete.html', {'transaction': transaction})

def kwaya_member_transaction_details(request, member_pk):
    transactions = KwayaMemberTransaction.objects.filter(member_id=member_pk).order_by('-transaction_date')
    total_amount_paid = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    return render(request, 'kwaya_member_transaction_details.html', {'transactions': transactions,'total_amount_paid': total_amount_paid})


# def kwaya_member_list(request):
#     kwaya_members = TmcsMember.objects.filter(vyama_vya_kitume='KWAYA')
#     return render(request, 'kwaya_member_list.html', {'kwaya_members': kwaya_members})


def kwaya_member_list(request):
    kwaya_members = TmcsMember.objects.filter(vyama_vya_kitume__icontains='KWAYA')
    # Fetching assigned voices for Kwaya members
    voice_assignments = KwayaVoiceAssignment.objects.filter(member__in=kwaya_members)
    # Creating a dictionary to store assigned voices for each member
    member_voices = {}
    for assignment in voice_assignments:
        member_id = assignment.member_id
        if member_id not in member_voices:
            member_voices[member_id] = []
        member_voices[member_id].append(assignment)
    return render(request, 'kwaya_member_list.html', {'kwaya_members': kwaya_members, 'member_voices': member_voices})


def kwaya_member_transactions(request):
    # Check if the current user is a member of the KWAYA group
    if request.user.is_authenticated:
        try:
            tmcs_member = TmcsMember.objects.get(email=request.user.email)
            if tmcs_member.vyama_vya_kitume == 'KWAYA':
                kwaya_transactions = KwayaMemberTransaction.objects.filter(member=tmcs_member)
                return render(request, 'kwaya_member_transactions.html', {'transactions': kwaya_transactions})
        except TmcsMember.DoesNotExist:
            pass
    return render(request, 'kwaya_member_transactions.html', {'message': 'You are not authorized to view this page.'})



@login_required
def individual_transactions(request):
    transactions = KwayaMemberTransaction.objects.filter(member=request.user)
    context = { 'transactions': transactions}
    return render(request, 'individual_transactions.html', context)


# def create_voice_assignment(request, member_id):
#     member = get_object_or_404(TmcsMember, id=member_id)
#     if request.method == 'POST':
#         form = KwayaVoiceAssignmentForm(request.POST)
#         if form.is_valid():
#             assignment = form.save(commit=False)
#             assignment.member = member
#             assignment.save()
#             return redirect('kwaya-member-list')
#     else:
#         form = KwayaVoiceAssignmentForm()
#     return render(request, 'create_voice_assignment.html', {'form': form, 'member': member})



from django.db import IntegrityError
from django.http import HttpResponse

def create_voice_assignment(request, member_id):
    member = get_object_or_404(TmcsMember, id=member_id)  # Get member from TmcsMember model
    existing_assignment = KwayaVoiceAssignment.objects.filter(member=member).first()
    if existing_assignment:
        return HttpResponse("Voice assignment already exists for this member.")
    
    if request.method == 'POST':
        form = KwayaVoiceAssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.member = member
            try:
                assignment.save()
                return redirect('kwaya-member-list')
            except IntegrityError:
                return HttpResponse("Error creating voice assignment.")
    else:
        form = KwayaVoiceAssignmentForm()
    return render(request, 'create_voice_assignment.html', {'form': form, 'member': member})



def update_voice_assignment(request, assignment_id):
    assignment = get_object_or_404(KwayaVoiceAssignment, id=assignment_id)
    if request.method == 'POST':
        form = KwayaVoiceAssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('kwaya-member-list')  # Redirect to member list after successful update
    else:
        form = KwayaVoiceAssignmentForm(instance=assignment)
    return render(request, 'update_voice_assignment.html', {'form': form, 'assignment': assignment})


def delete_voice_assignment(request, assignment_id):
    assignment = get_object_or_404(KwayaVoiceAssignment, id=assignment_id)
    if request.method == 'POST':
        assignment.delete()
        return redirect('kwaya-member-list')
    return render(request, 'delete_voice_assignment.html', {'assignment': assignment})


def achievements_view(request):
    achievements = Achievement.objects.all().order_by('position')
    return render(request, 'achievements.html', {'achievements': achievements})