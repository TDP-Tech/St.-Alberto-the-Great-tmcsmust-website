from django import forms
# from multiselectfield import MultiSelectField  # Ensure you have this package installed
from .models import TmcsMember, VYAMA_VYA_KITUME

class TmcsMemberForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = TmcsMember
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'namba_ya_mwanafunzi', 'email', 
                  'namba_ya_mzazi', 'ubatizo', 'kipaimara', 'ndoa_au_daraja', 'elimu_uliyonayo', 
                  'parokia', 'jimbo_kuu', 'course', 'department', 'college', 'level_of_study', 
                  'vyama_vya_kitume', 'vinginevyo', 'is_staff', 'is_superuser', 'is_active',
                  'is_mwenyekiti_tawi', 'is_katibu_tawi', 'is_mhazini_tawi',
                  'is_mwenyekiti_mipango_na_fedha','is_katibu_mipango_na_fedha','is_mhazini_mipango_na_fedha',
                  'is_mwenyekiti_legio','is_katibu_legio','is_mhazini_legio',
                  'is_mwenyekiti_kwaya','is_katibu_kwaya','is_mhazini_kwaya',
                  'is_mwenyekiti_karismatiki','is_katibu_karismatiki','is_mhazini_karismatiki',
                  'is_mwenyekiti_moyo_mtakatifu_wa_Yesu','is_katibu_moyo_mtakatifu_wa_Yesu',
                  'is_mhazini_moyo_mtakatifu_wa_Yesu', 'is_kiongozi_wa_darasa',
                  'is_mwenyekiti_litrujia','is_katibu_litrujia', 'is_registration_committee',
                  ]
                  
        labels = {
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'namba_ya_mwanafunzi': 'Student Phone Number',
            'email': 'Email',
            'namba_ya_mzazi': "Parent's Phone Number",
            'ubatizo': 'Ubatizo',
            'kipaimara': 'Kipaimara',
            'ndoa_au_daraja': 'Ndoa/Daraja',
            'elimu_uliyonayo': 'Elimu uliyonayo kwa sasa',
            'parokia': 'Parokia',
            'jimbo_kuu': 'Jimbo Kuu',
            'course': 'Course unayosoma sasa',
            'department': 'Department',
            'college': 'College',
            'level_of_study': 'Level ya elimu unayosoma sasa',
            'vyama_vya_kitume': 'Chama vya kitume',
            'vinginevyo': 'Vinginevyo',
            'is_staff': 'Is Staff',
            'is_active': 'Is Active',
        }
    
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'namba_ya_mwanafunzi': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'namba_ya_mzazi': forms.TextInput(attrs={'class': 'form-control'}),
            'ubatizo': forms.Select(attrs={'class': 'form-control'}),
            'kipaimara': forms.Select(attrs={'class': 'form-control'}),
            'ndoa_au_daraja': forms.Select(attrs={'class': 'form-control'}),
            'elimu_uliyonayo': forms.Select(attrs={'class': 'form-control'}),
            'parokia': forms.TextInput(attrs={'class': 'form-control'}),
            'jimbo_kuu': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-control'}),
            'level_of_study': forms.Select(attrs={'class': 'form-control'}),
            'vyama_vya_kitume': forms.SelectMultiple(attrs={'class': 'form-control select-multiple'}),
            'vinginevyo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Acha wazi kama hakuna'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
