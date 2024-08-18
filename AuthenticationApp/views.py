from django.shortcuts import render
from .models import TmcsMember
from .forms import TmcsMemberForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def register_member(request):
    if request.method == 'POST':
        form = TmcsMemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            messages.success(request, f'Member {member.first_name.upper()} {member.middle_name.upper()} {member.last_name.upper()} registered successfully!')
            return redirect('member-list')
        else:
            if 'password1' in form.errors and 'password2' in form.errors:
                messages.error(request, "Passwords do not match.")
            elif 'email' in form.errors:
                messages.error(request, "Email already exists. Create unique one")
            else:
                # Add error messages for other fields if needed
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = TmcsMemberForm()
    return render(request, 'register_member.html', {'form':form})



from django.db.models import Q

def member_list(request):
    query = request.GET.get('q', '')  # Get the search query from the request

    # Filter members based on the search query
    members = TmcsMember.objects.filter(
        Q(first_name__icontains=query) |  # Search by first name (case-insensitive)
        Q(last_name__icontains=query) |   # Search by last name (case-insensitive)
        Q(course__icontains=query) |       # Search by course (case-insensitive)
        Q(namba_ya_mwanafunzi__icontains=query) | # Search by phone number (case-insensitive)
        Q(email__icontains=query)          # Search by email (case-insensitive)
        # Add other fields as needed
    )

    return render(request, 'member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(TmcsMember, pk=pk)
    return render(request, 'member_detail.html', {'member': member})

def member_update(request, pk):
    member = get_object_or_404(TmcsMember, pk=pk)
    if request.method == 'POST':
        form = TmcsMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member-list')
    else:
        form = TmcsMemberForm(instance=member)
    return render(request, 'member_update.html', {'form': form, 'member': member})

def member_delete(request, pk):
    member = get_object_or_404(TmcsMember, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member-list')
    return render(request, 'member_delete.html', {'member': member})
