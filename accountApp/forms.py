# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile


class BootstrapStyleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control col-md-12'})
            
class SignUpForm(UserCreationForm, BootstrapStyleForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return password2
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control', 'placeholder':'use your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'enter password'}))

    error_messages = {
        'invalid_login': "Please enter a correct email and password. Note that both fields may be case-sensitiveeeeeeeeeee.",
        'inactive': "This account is inactive.",
    }

    class Meta:
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'displayname', 'carrier']
        labels = {
            'image': 'Profile Image',
            'displayname': 'Display Name',
            'carrier': 'Carrier',
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'displayname': forms.TextInput(attrs={'class': 'form-control'}),
            'carrier': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

