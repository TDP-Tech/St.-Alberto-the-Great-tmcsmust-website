from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Community, Rozary, CommitteeMember, Novena, SaintLife, Image, MaswalinaMajibu, MasomoyaDominika, NewsItem, Quote, Event, CalenderYaTMCSTawiPDF, LeadersTeamMember
from . forms import CommunityForm, RozaryForm, NovenaForm, SaintLifeForm, ImageUploadForm, MaswalinaMajibuForm, MasomoyaDominikaForm,CommitteeMemberForm, NewsItemForm, QuoteForm, EventForm, CalenderYaTMCSTawiPDFUploadForm, FeedbackForm, ContactForm, LeadersTeamMemberForm
from kwayaApp.models import Achievement
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date

########################
def welcome_page(request):
    news_items = NewsItem.objects.order_by('-id')[:9]
    quotes = Quote.objects.order_by('-id')[:1]
    current_date = date.today().strftime("%B %d, %Y")  # Get current date
    events = Event.objects.order_by('-date')
    achievements = Achievement.objects.order_by('-id')[:10]
    # Handle feedback form submission
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return HttpResponseRedirect(reverse('welcome_page') + '#feedbacks')
            # Optionally, redirect to a thank you page or refresh the current page
    else:
        feedback_form = FeedbackForm()  # Create a new instance of the feedback form
    return render(request, 'welcome_page.html', {'news_items':news_items,'quotes':quotes, 'date':current_date, 'events':events, 'feedback_form':feedback_form, 'achievements':achievements })

def gradient(request):
    return render(request, 'gradient.html', {'active_link': 'gradient'})


#########################
def MaswaliNaMajibu(request):
    return render(request, 'maswali_na_majibu.html', {'active_link': 'MaswaliNaMajibu'})

def MaswaliNaMajibu_list(request):
    MaswaliNaMajibu = MaswalinaMajibu.objects.all().order_by('-id')
    return render(request, 'MaswaliNaMajibu_list.html', {'MaswaliNaMajibu': MaswaliNaMajibu})

def MaswaliNaMajibu_detail(request, pk):
    MaswaliNaMajibu = get_object_or_404(MaswalinaMajibu, pk=pk)
    return render(request, 'MaswaliNaMajibu_detail.html', {'MaswaliNaMajibu': MaswaliNaMajibu})

def MaswaliNaMajibu_create(request):
    if request.method == 'POST':
        form = MaswalinaMajibuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maswalinamajibu-list')
    else:
        form = MaswalinaMajibuForm()
    return render(request, 'maswalinamajibu_create.html', {'form': form})

def MaswaliNaMajibu_update(request, pk):
    MaswaliNaMajibu = get_object_or_404(MaswalinaMajibu, pk=pk)
    if request.method == 'POST':
        form = MaswalinaMajibuForm(request.POST, instance=MaswaliNaMajibu)
        if form.is_valid():
            form.save()
            return redirect('maswalinamajibu-detail', pk=MaswaliNaMajibu.pk)
    else:
        form = MaswalinaMajibuForm(instance=MaswaliNaMajibu)
    return render(request, 'maswalinamajibu_update.html', {'form': form})

def MaswaliNaMajibu_delete(request, pk):
    MaswaliNaMajibu = get_object_or_404(MaswalinaMajibu, pk=pk)
    if request.method == 'POST':
        MaswaliNaMajibu.delete()
        return redirect('maswalinamajibu-list')
    return render(request, 'maswalinamajibu_delete.html', {'MaswaliNaMajibu': MaswaliNaMajibu})

#########################
def masomoya_dominika_create(request):
    if request.method == 'POST':
        form = MasomoyaDominikaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('masomoya-dominika-list')
    else:
        form = MasomoyaDominikaForm()
    return render(request, 'masomoyadominika_create.html', {'form': form})

def masomoya_dominika_list(request):
    masomoyadominika_list = MasomoyaDominika.objects.all().order_by('-id')
    return render(request, 'masomoyadominika_list.html', {'masomoyadominika_list': masomoyadominika_list})

def masomoya_dominika_detail(request, pk):
    masomoyadominika = get_object_or_404(MasomoyaDominika, pk=pk)
    return render(request, 'masomoyadominika_detail.html', {'masomoyadominika': masomoyadominika})

def masomoya_dominika_update(request, pk):
    masomoyadominika = get_object_or_404(MasomoyaDominika, pk=pk)
    if request.method == 'POST':
        form = MasomoyaDominikaForm(request.POST, instance=masomoyadominika)
        if form.is_valid():
            form.save()
            return redirect('masomoya-dominika-detail', pk=pk)
    else:
        form = MasomoyaDominikaForm(instance=masomoyadominika)
    return render(request, 'masomoyadominika_update.html', {'form': form})

def masomoya_dominika_delete(request, pk):
    masomoyadominika = get_object_or_404(MasomoyaDominika, pk=pk)
    if request.method == 'POST':
        masomoyadominika.delete()
        return redirect('masomoya-dominika-list')
    return render(request, 'masomoyadominika_delete.html', {'masomoyadominika': masomoyadominika})
#########################

#########################
#########################
#########################
#########################

def Michezo(request):
    return render(request, 'michezo.html', {'active_link': 'Michezo'})

def Muziki(request):
    return render(request, 'muziki.html', {'active_link': 'Muziki'})

def MipangoNaFedha(request):
    return render(request, 'mipango_na_fedha.html', {'active_link': 'MipangoNaFedha'})
#########################
#########################
#########################
#########################


#######################
def rozary_create(request):
    if request.method == 'POST':
        form = RozaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rozary-list')
    else:
        form = RozaryForm()
    return render(request, 'rozary_create.html', {'form': form})

def rozary_list(request):
    query = request.GET.get('q', '')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        rozaries = Rozary.objects.filter(rozary_name__icontains=query)
        data = []
        for rozary in rozaries:
            data.append({
                'id': rozary.id,
                'rozary_name': rozary.rozary_name,
                'description': rozary.description,
                'rozary_image': request.build_absolute_uri(rozary.rozary_image.url)
            })
        return JsonResponse(data, safe=False)
    rozaries = Rozary.objects.filter(rozary_name__icontains=query)
    return render(request, 'rozary_list.html', {'rozaries': rozaries, 'query': query})

def rozary_detail(request, pk):
    rozary = get_object_or_404(Rozary, pk=pk)
    return render(request, 'rozary_detail.html', {'rozary': rozary})

def rozary_update(request, pk):
    rozary = get_object_or_404(Rozary, pk=pk)
    if request.method == 'POST':
        form = RozaryForm(request.POST, request.FILES, instance=rozary)
        if form.is_valid():
            form.save()
            return redirect('rozary-detail', pk=rozary.pk)
    else:
        form = RozaryForm(instance=rozary)
    return render(request, 'rozary_update.html', {'form': form, 'rozary': rozary})

def rozary_pdf_download(request, pk):
    rozary = get_object_or_404(Rozary, pk=pk)
    template_path = 'rozary_pdf_template.html'
    # Create an absolute URL for the image
    absolute_image_url = request.build_absolute_uri(rozary.rozary_image.url)
    context = {'rozary': rozary, 'absolute_image_url':absolute_image_url}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{rozary.rozary_name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def rozary_delete(request, pk):
    rozary = get_object_or_404(Rozary, pk=pk)
    if request.method == 'POST':
        rozary.delete()
        return redirect('rozary-list')
    return render(request, 'rozary_delete.html', {'rozary': rozary})

#######################
def novena_create(request):
    if request.method == 'POST':
        form = NovenaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('novena-list')
    else:
        form = NovenaForm()
    return render(request, 'novena_create.html', {'form': form})

# def novena_list(request):
#     novenas = Novena.objects.all()
#     return render(request, 'novena_list.html', {'novenas': novenas})

def novena_list(request):
    query = request.GET.get('q', '')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        novenas = Novena.objects.filter(novena_name__icontains=query)
        data = []
        for novena in novenas:
            data.append({
                'id': novena.id,
                'novena_name': novena.novena_name,
                'description': novena.description,
                'novena_image': request.build_absolute_uri(novena.novena_image.url)
            })
        return JsonResponse(data, safe=False)
    novenas = Novena.objects.filter(novena_name__icontains=query)
    return render(request, 'novena_list.html', {'novenas': novenas, 'query': query})


def novena_detail(request, pk):
    novena = get_object_or_404(Novena, pk=pk)
    return render(request, 'novena_detail.html', {'novena': novena})

def novena_update(request, pk):
    novena = get_object_or_404(Novena, pk=pk)
    if request.method == 'POST':
        form = NovenaForm(request.POST, request.FILES, instance=novena)
        if form.is_valid():
            form.save()
            return redirect('novena-detail', pk=novena.pk)
    else:
        form = NovenaForm(instance=novena)
    return render(request, 'novena_update.html', {'form': form, 'novena': novena})

def novena_pdf_download(request, pk):
    novena = get_object_or_404(Novena, pk=pk)
    template_path = 'novena_pdf_template.html'
    # Create an absolute URL for the image
    absolute_image_url = request.build_absolute_uri(novena.novena_image.url)
    context = {'novena': novena, 'absolute_image_url': absolute_image_url}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{novena.novena_name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def novena_delete(request, pk):
    novena = get_object_or_404(Novena, pk=pk)
    if request.method == 'POST':
        novena.delete()
        return redirect('novena-list')
    return render(request, 'novena_delete.html', {'novena': novena})

######################
def community_create(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('community-list')
    else:
        form = CommunityForm()
    return render(request, 'community_create.html', {'form': form})

def community_list(request):
    communities = Community.objects.all()
    return render(request, 'community_list.html', {'communities': communities})

def community_detail(request, pk):
    community = get_object_or_404(Community, pk=pk)
    return render(request, 'community_detail.html', {'community': community})


def community_update(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES, instance=community)
        if form.is_valid():
            form.save()
            return redirect('community-list')
    else:
        form = CommunityForm(instance=community)
    return render(request, 'community_update.html', {'form': form})

def community_delete(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if request.method == 'POST':
        community.delete()
        return redirect('community-list')
    return render(request, 'community_delete.html', {'community': community})

#####################################

def committee_create(request):
    if request.method == 'POST':
        form = CommitteeMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('committee-list')
    else:
        form = CommitteeMemberForm()
    return render(request, 'committee_create.html', {'form': form})

def committee_list(request):
    members_commitee_list = CommitteeMember.objects.all()
    return render(request, 'committee_list.html', {'members_commitee_list': members_commitee_list})

def committee_detail(request, pk):
    committee_member = get_object_or_404(CommitteeMember, pk=pk)
    return render(request, 'committee_detail.html', {'committee_member': committee_member})

def committee_update(request, pk):
    committee_member = get_object_or_404(CommitteeMember, pk=pk)
    if request.method == 'POST':
        form = CommitteeMemberForm(request.POST, request.FILES, instance=committee_member)
        if form.is_valid():
            form.save()
            return redirect('committee-list')
    else:
        form = CommitteeMemberForm(instance=committee_member)
    return render(request, 'committee_update.html', {'form': form})

def committee_delete(request, pk):
    committee_member = get_object_or_404(CommitteeMember, pk=pk)
    if request.method == 'POST':
        committee_member.delete()
        return redirect('committee-list')
    return render(request, 'committee_delete.html', {'committee_member': committee_member})

#####################################
# def saintlife_list(request):
#     saints = SaintLife.objects.all()
#     return render(request, 'saintlife_list.html', {'saints': saints})

def saintlife_list(request):
    query = request.GET.get('q', '')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        saints = SaintLife.objects.filter(name_of_saint__icontains=query)
        data = []
        for saint in saints:
            data.append({
                'id': saint.id,
                'name_of_saint': saint.name_of_saint,
                'biography': saint.biography,
                'image': request.build_absolute_uri(saint.image.url)
            })
        return JsonResponse(data, safe=False)
    saints = SaintLife.objects.filter(name_of_saint__icontains=query)
    return render(request, 'saintlife_list.html', {'saints': saints, 'query': query})



def saintlife_detail(request, pk):
    saint = get_object_or_404(SaintLife, pk=pk)
    return render(request, 'saintlife_detail.html', {'saint': saint})

def saintlife_create(request):
    if request.method == 'POST':
        form = SaintLifeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('saintlife-list'))
    else:
        form = SaintLifeForm()
    return render(request, 'saintlife_create.html', {'form': form})

def saintlife_update(request, pk):
    saint = get_object_or_404(SaintLife, pk=pk)
    if request.method == 'POST':
        form = SaintLifeForm(request.POST, request.FILES, instance=saint)
        if form.is_valid():
            form.save()
            return redirect(reverse('saintlife-list'))
    else:
        form = SaintLifeForm(instance=saint)
    return render(request, 'saintlife_update.html', {'form': form})

def saintlife_delete(request, pk):
    saint = get_object_or_404(SaintLife, pk=pk)
    if request.method == 'POST':
        saint.delete()
        return redirect(reverse('saintlife-list'))
    return render(request, 'saintlife_delete.html', {'saint': saint})

def saintlife_pdf_download(request, pk):
    saint = get_object_or_404(SaintLife, pk=pk)
    template_path = 'saintlife_pdf_template.html'
    # Create an absolute URL for the image
    absolute_image_url = request.build_absolute_uri(saint.image.url)
    context = {'saint': saint, 'absolute_image_url': absolute_image_url}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{saint.name_of_saint}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

####################################
def historia_ya_tmcs(request):
    return render(request, 'historia_ya_tmcs.html')

def historia_ya_imcs(request):
    return render(request, 'historia_ya_imcs.html')

####################################
def event_image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image')
            for img in images:
                Image.objects.create(user=request.user, image=img)
            return redirect('event-image-gallery')
    else:
        form = ImageUploadForm()
    return render(request, 'event_image_upload.html', {'form': form})

def event_image_gallery(request):
    images = Image.objects.all()
    return render(request, 'event_image_gallery.html', {'images': images})
####################################

def news_create(request):
    if request.method == 'POST':
        form = NewsItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('welcome_page') + '#newslist')
    else:
        form = NewsItemForm()
    return render(request, 'news_create.html', {'form': form})

def news_list(request):
    news_items = NewsItem.objects.order_by('-id')
    return render(request, 'news_list.html', {'news_items': news_items})

def news_detail(request, pk):   
    news_item = get_object_or_404(NewsItem, pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})

def news_update(request, pk):
    news_item = get_object_or_404(NewsItem, pk=pk)
    if request.method == 'POST':
        form = NewsItemForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('welcome_page') + '#newslist')
    else:
        form = NewsItemForm(instance=news_item)
    return render(request, 'news_update.html', {'form': form})

def news_delete(request, pk):
    news_item = get_object_or_404(NewsItem, pk=pk)
    if request.method == 'POST':
        news_item.delete()
        return redirect('news-list')
    # If the request method is not POST, render a confirmation page
    return render(request, 'news_delete.html', {'news_item': news_item})



def quote_create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_list')  # Redirect to list view after successful creation
    else:
        form = QuoteForm()
    return render(request, 'quote_create.html', {'form': form})

def quote_update(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_list')  # Redirect to list view after successful update
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'quote_update.html', {'form': form})

def quote_delete(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        quote.delete()
        return redirect('quote_list')  # Redirect to list view after successful deletion
    return render(request, 'quote_delete.html', {'quote': quote})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to list view after successful creation
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to list view after successful update
    else:
        form = EventForm(instance=event)
    return render(request, 'event_update.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')  # Redirect to list view after successful deletion
    return render(request, 'event_delete.html', {'event': event})


def upload_calender_ya_tawi_pdf(request):
    if request.method == 'POST':
        form = CalenderYaTMCSTawiPDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('calenda-pdf-list')
    else:
        form = CalenderYaTMCSTawiPDFUploadForm()
    return render(request, 'calenda_ya_tawi_create.html', {'form': form})

def calenda_ya_tawi_list(request):
    pdf_files = CalenderYaTMCSTawiPDF.objects.all()
    return render(request, 'calenda_list.html', {'pdf_files': pdf_files})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your feedback has been submitted successfully!')
            return redirect('feedback-success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-success')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def about_us(request):
    national_leaders = LeadersTeamMember.objects.filter(level='National Leader')
    zonal_leaders = LeadersTeamMember.objects.filter(level='Zonal Leader')
    branch_leaders = LeadersTeamMember.objects.filter(level='Branch Leader')
    
    context = {
        'national_leaders': national_leaders,
        'zonal_leaders': zonal_leaders,
        'branch_leaders': branch_leaders,
    }
    
    return render(request, 'about_us.html', context)

def leader_add(request):
    if request.method == 'POST':
        form = LeadersTeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about-us')
    else:
        form = LeadersTeamMemberForm()
    return render(request, 'leader_add.html', {'form': form})

def leader_edit(request, pk):
    leader = get_object_or_404(LeadersTeamMember, pk=pk)
    if request.method == 'POST':
        form = LeadersTeamMemberForm(request.POST, request.FILES, instance=leader)
        if form.is_valid():
            form.save()
            return redirect('about-us')
    else:
        form = LeadersTeamMemberForm(instance=leader)
    return render(request, 'leader_edit.html', {'form': form})

def leader_delete(request, pk):
    leader = get_object_or_404(LeadersTeamMember, pk=pk)
    if request.method == 'POST':
        leader.delete()
        return redirect('about-us')
    return render(request, 'leader_delete.html', {'leader': leader})


