from dataclasses import fields
from posts.models import Profile
from re import template
from turtle import mode
from unittest import mock
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from .forms import EditProfileForm

# Create your views here.

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'members/edit_profile_page.html'
    fields = [
    'bio',
    'profile_image',
    'website_url',
    'facebook_url',
    'twitter_url',
    'instagram_url',
    'linkedin_url'
    ]
    success_url =  reverse_lazy('posts:home')


class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'members/show_user_profile.html'
    def get_context_data(self,*args ,**kwargs):
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        user_page = get_object_or_404(Profile,id = self.kwargs['pk'])
        context['user_page'] = user_page
        return context

def user_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request,"Password does not match")
            return redirect('members:register')
        elif User.objects.filter(username=username).exists():
            messages.warning(request,"Username already taken")
            return redirect('members:register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,"Email already taken")
            return redirect('members:register')
        else:
            user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            username= username,
            email = email,
            password = password1,
            )
            user.save()
            messages.success(request,'User has been registered successully')
            return redirect('members:login')
    return render(request,'members/register.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        # the fist username and password comming from the database
        if user is not None:
            login(request,user)
            return redirect('posts:home')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('members:login')
    return render(request,'members/login.html')

def user_logout(request):
    logout(request)
    return redirect("posts:home")



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'members/editprofile.html'
    success_url = reverse_lazy('posts:home')
    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url =  reverse_lazy('posts:home')
