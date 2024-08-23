from django.shortcuts import render, redirect
from .forms import ViongoziWaMadarasaForm
from .models import ViongoziWaMadarasa
from AuthenticationApp.models import TmcsMember
from django.db.models import Q

def create_class_leader(request):
    if request.method == 'POST':
        form = ViongoziWaMadarasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class-members')
    else:
        form = ViongoziWaMadarasaForm()
    return render(request, 'create_class_leader.html', {'form': form})


# def leader_list(request):
#     leaders = ViongoziWaMadarasa.objects.all()
#     return render(request, 'leader_list.html', {'leaders': leaders})

from django.shortcuts import render
from django.db.models import Q
from .models import TmcsMember  # Adjust the import based on your actual app structure

def leader_list(request, role=None):
    # Define role-to-filter mappings
    role_filters = {
        'kamati-kuu': ['is_mwenyekiti_tawi', 'is_katibu_tawi', 'is_mhazini_tawi'],
        'litrujia': ['is_mwenyekiti_litrujia', 'is_katibu_litrujia'],
        'mipango-na-fedha': ['is_mwenyekiti_mipango_na_fedha', 'is_katibu_mipango_na_fedha', 'is_mhazini_mipango_na_fedha'],
        'mas-media': ['is_mwenyekiti_mas_media', 'is_katibu_mas_media', 'is_mhazini_mas_media'],
        'sherehe-na-maafa': ['is_mwenyekiti_sherehe_na_maafa', 'is_katibu_sherehe_na_maafa', 'is_mhazini_sherehe_na_maafa'],
        'michezo-na-burudani': ['is_mwenyekiti_michezo_na_burudani', 'is_katibu_michezo_na_burudani', 'is_mhazini_michezo_na_burudani'],
        'muziki': ['is_mwenyekiti_muziki', 'is_katibu_muziki', 'is_mhazini_muziki'],
        'elimu-ushauri-na-nidhamu': ['is_mwenyekiti_elimu_ushauri_na_nidhamu', 'is_katibu_elimu_ushauri_na_nidhamu', 'is_mhazini_elimu_ushauri_na_nidhamu'],
        'kwaya': ['is_mwenyekiti_kwaya', 'is_katibu_kwaya', 'is_mhazini_kwaya'],
        'legio': ['is_mwenyekiti_legio', 'is_katibu_legio', 'is_mhazini_legio'],
        'karismatiki': ['is_mwenyekiti_karismatiki', 'is_katibu_karismatiki', 'is_mhazini_karismatiki'],
        'moyo-mtakatifu-wa-Yesu': ['is_mwenyekiti_moyo_mtakatifu_wa_Yesu', 'is_katibu_moyo_mtakatifu_wa_Yesu', 'is_mhazini_moyo_mtakatifu_wa_Yesu'],
        'kiongozi-wa-darasa': ['is_kiongozi_wa_darasa'],
        'registration-committee': ['is_registration_committee'],
    }

    # Determine which roles to filter by
    filter_keys = role_filters.get(role, [])

    if filter_keys:
        filter_args = Q()
        for key in filter_keys:
            filter_args |= Q(**{key: True})
        leaders = TmcsMember.objects.filter(filter_args)
    else:
        leaders = TmcsMember.objects.none()  # Return an empty queryset if no role matches

    # Preprocess the role string for display purposes
    if role:
        role_display = role.replace('-', ' ').replace('_', ' ').title()
    else:
        role_display = "Madarasa"

    context = {
        'leaders': leaders,
        'role': role_display,
    }
    return render(request, 'leader_list.html', context)



def update_class_leader(request, pk):
    class_leader = ViongoziWaMadarasa.objects.get(pk=pk)
    if request.method == 'POST':
        form = ViongoziWaMadarasaForm(request.POST, instance=class_leader)
        if form.is_valid():
            form.save()
            return redirect('leader-list')
    else:
        form = ViongoziWaMadarasaForm(instance=class_leader)
    return render(request, 'update_class_leader.html', {'form': form})

def delete_class_leader(request, pk):
    class_leader = ViongoziWaMadarasa.objects.get(pk=pk)
    if request.method == 'POST':
        class_leader.delete()
        return redirect('leader-list')
    return render(request, 'delete_class_leader.html', {'class_leader': class_leader})

# def class_members(request):
#     # Assuming the class leader is associated with a specific course and level of study
#     class_leader = request.user.class_leader  # Assuming class_leader is linked to user
#     # Access the associated TmcsMember
#     tmcs_member = class_leader.user
#     # Retrieve class members with the same course and level of study as the class leader
#     class_members = TmcsMember.objects.filter(course=tmcs_member.course, level_of_study=tmcs_member.level_of_study)
#     return render(request, 'class_members.html', {'class_members': class_members})

from django.contrib import messages

def class_members(request):
    current_user = request.user
    
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to view this page.')
        return redirect('/accounts/login/')  # Redirect to the login page or another page of your choice

    # Get the user object for the current user

    # Initialize class_leader variable to None
    class_leader = None

    # Check if the current user has any of the leadership roles
    if (
        current_user.is_mwenyekiti_tawi or
        current_user.is_katibu_tawi or
        current_user.is_mhazini_tawi or
        current_user.is_mwenyekiti_legio or
        current_user.is_katibu_legio or
        current_user.is_mhazini_legio or
        current_user.is_mwenyekiti_kwaya or
        current_user.is_katibu_kwaya or
        current_user.is_mhazini_kwaya or
        current_user.is_mwenyekiti_karismatiki or
        current_user.is_katibu_karismatiki or
        current_user.is_mhazini_karismatiki or
        current_user.is_mwenyekiti_moyo_mtakatifu_wa_Yesu or
        current_user.is_katibu_moyo_mtakatifu_wa_Yesu or
        current_user.is_mhazini_moyo_mtakatifu_wa_Yesu or
        current_user.is_kiongozi_wa_darasa or
        current_user.is_mwenyekiti_litrujia or
        current_user.is_katibu_litrujia or
        current_user.is_mwenyekiti_mipango_na_fedha or
        current_user.is_katibu_mipango_na_fedha or
        current_user.is_mhazini_mipango_na_fedha or
        current_user.is_registration_committee
    ):
        # If the user has any leadership role, set class_leader to the current user
        class_leader = current_user

    # Retrieve class members with the same course and level of study as the class leader
    tmcs_members = TmcsMember.objects.filter(course=current_user.course, level_of_study=current_user.level_of_study)

    return render(request, 'class_members.html', {'class_leader': class_leader, 'class_members': tmcs_members})
