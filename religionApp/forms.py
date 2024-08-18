from django import forms
from .models import Community, Rozary, Novena, SaintLife, Image, MaswalinaMajibu, MasomoyaDominika, CommitteeMember, NewsItem, Quote, Event, CalenderYaTMCSTawiPDF, Feedback, ContactMessage, LeadersTeamMember
from django_ckeditor_5.widgets import CKEditor5Widget



class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['community_name', 'description', 'community_image', 'patron_saint']
        labels = {
            'community_name': 'Community Name',
            'description': 'Description',
            'community_image': 'Community Image',
            'patron_saint': 'Patron Saint',
        }
        widgets = {
            'community_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Eg: JUMUIYA YA MT. ANTHONY WA PADUA'}),
            'description': CKEditor5Widget(),
            'community_image': forms.FileInput(attrs={'class': 'form-control'}),
            'patron_saint': forms.Select(attrs={'class': 'form-control'}),
        }
 
class RozaryForm(forms.ModelForm):
    class Meta:
        model = Rozary
        fields = ['rozary_name', 'description', 'rozary_image']

        labels = {
            'rozary_name': 'Rozary Name',
            'description': 'Description',
            'rozary_image': 'Rozary Image',
        }

        widgets = {
            'rozary_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': CKEditor5Widget(),
            'rozary_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
class NovenaForm(forms.ModelForm):
    class Meta:
        model = Novena
        fields = ['novena_name', 'description', 'novena_image']

        labels = {
            'novena_name': 'Novena Name',
            'description': 'Description',
            'novena_image': 'Novena Image',
        }

        widgets = {
            'novena_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': CKEditor5Widget(),
            'novena_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SaintLifeForm(forms.ModelForm):
    class Meta:
        model = SaintLife
        fields = ['name_of_saint', 'birth_date', 'death_date', 'biography', 'image']

        labels = {
            'name_of_saint': 'Saint Name',
            'birth_date': 'Date of Birth',
            'death_date': 'Date of Death',
            'biography': 'Biography',
            'image': 'Image',
        }

        widgets = {
            'name_of_saint': forms.TextInput(attrs={'class': 'form-control col-md-5'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control col-md-5'}),
            'death_date': forms.DateInput(attrs={'class': 'form-control col-md-5'}),
            'biography': CKEditor5Widget(),
            'image': forms.FileInput(attrs={'class': 'form-control col-md-5'}),
        }

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','title']
        widgets = {
            # 'image': forms.ClearableFileInput(attrs={'multiple': True}),
            'image': forms.ClearableFileInput(),
            'title': forms.TextInput(attrs={'class': 'form-control col-md-3'}),
        }
        
class MaswalinaMajibuForm(forms.ModelForm):
    class Meta:
        model = MaswalinaMajibu
        fields = ['swali', 'jibu']
        widgets = {
            'swali': CKEditor5Widget(),
            'jibu': CKEditor5Widget(),
        }
        
class MasomoyaDominikaForm(forms.ModelForm):
    class Meta:
        model = MasomoyaDominika
        fields = ['dominika', 'somo_la1', 'somo_la2', 'injili']
        widgets = {
            'somo_la1': CKEditor5Widget(),
            'somo_la2': CKEditor5Widget(),
            'injili': CKEditor5Widget(),
            'dominika': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CommitteeMemberForm(forms.ModelForm):
    class Meta:
        model = CommitteeMember
        fields = ['nafasi_ya_uongozi', 'jina_la_kiongozi', 'picha_ya_kiongozi', 'kozi_anayosoma', 'phone_number']

        labels = {
            'nafasi_ya_uongozi': 'Position',
            'jina_la_kiongozi': 'Leader Name',
            'picha_ya_kiongozi': 'Leader Image',
            'kozi_anayosoma': 'Course',
            'phone_number': 'Phone Number',
        }

        widgets = {
            'nafasi_ya_uongozi': forms.TextInput(attrs={'class': 'form-control'}),
            'jina_la_kiongozi': forms.TextInput(attrs={'class': 'form-control'}),
            'picha_ya_kiongozi': forms.FileInput(attrs={'class': 'form-control'}),
            'kozi_anayosoma': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class NewsItemForm(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = ['title', 'description']
        
        labels = {
            'title': 'Title of the News',
            'description': 'Description',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text_quote', 'author_of_quote']

        labels = {
            'text_quote': 'Quote Text',
            'author_of_quote': 'Author',
        }

        widgets = {
            'text_quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'author_of_quote': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','image','event_date']

        labels = {
            'title': 'Event Title',
            'image': 'Event Image',
            'event_date': 'Event Date',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CalenderYaTMCSTawiPDFUploadForm(forms.ModelForm):
    class Meta:
        model = CalenderYaTMCSTawiPDF
        fields = ['pdf_title','pdf_file']
        
        labels = {
            'pdf_title': 'PDF Title',
            'pdf_file': 'PDF File',
        }

        widgets = {
            'pdf_title': forms.TextInput(attrs={'class': 'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        
        labels = {
            'name': '',
            'email': '',
            'message': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'enter your Name here'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'enter your e-mail'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 4, 'placeholder':'Type your message or feedback here'}),
        }
        



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['user_name', 'email', 'message']

class LeadersTeamMemberForm(forms.ModelForm):
    class Meta:
        model = LeadersTeamMember
        fields = ['leader_name', 'leader_position', 'image', 'level', 'start_year', 'end_year', 'contact_info']
        labels = {
            'leader_name': 'Leader Name',
            'leader_position': 'Leader Position',
            'image': 'Profile Image',
            'level': 'Leadership Level',
            'start_year': 'Start Year',
            'end_year': 'End Year',
            'contact_info': 'Contact Information',
        }
        widgets = {
            'leader_name': forms.TextInput(attrs={'class': 'form-control'}),
            'leader_position': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'start_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'end_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
