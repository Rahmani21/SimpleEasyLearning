from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from posts.models import Profile


class EditProfileForm(UserChangeForm):
    email = forms.CharField(widget=forms.EmailInput(attrs = {'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password','last_login','is_superuser','is_staff','is_active','date_joined')



'Createe_user_profile_Page'
class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ('bio','profile_image','website_url','facebook_url','twitter_url','instagram_url','linkedin_url')

        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control'}),
                # 'profile_image':forms.TextInput(attrs={'class':'form-control'}),
                'website_url':forms.TextInput(attrs={'class':'form-control'}),
                'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
                'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
                'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
                'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
        }
