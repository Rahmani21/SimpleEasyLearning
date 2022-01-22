from ast import arg
from audioop import reverse
from dataclasses import fields
from gc import get_objects
from importlib.resources import path
from operator import mod
from pyexpat import model
from re import template
from statistics import mode
from types import CellType
from unittest import mock
from django.shortcuts import render,redirect,get_object_or_404
from django.template import context
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Category, Post

# from posts.models import Post
from .forms import PostForm,UpdateForm
# Create your views here.
def likeView(request,pk):
    post = get_object_or_404(Post,id = request.POST.get('post_id'))
    # post = get_objects(Post,id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('posts:details',args = [str(pk)]))
    # return redirect(reverse('posts:details',args = [(pk)]))
    # return redirect('posts/details.html',args = [(pk)])
    # return redirect('posts:details')
class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    ordering = ['-post_date']
    # for category
    def get_context_data(self,*args ,**kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context['category_menu'] = category_menu
        return context


    

class DetailsVeiw(DetailView):
    model = Post
    template_name = 'posts/details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/add_post.html"
    # fields = "__all__"

    def get_context_data(self,*args ,**kwargs):
        category_menu = Category.objects.all()
        context = super(AddPostView,self).get_context_data(*args,**kwargs)
        context['category_menu'] = category_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "posts/add_category.html"
    fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'posts/update_post.html'
    

class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy('posts:home')



def categoryview(request,category):
    category_post = Post.objects.filter(category = category.replace('-',' '))
    context = {
        'category':category.title().replace('-',' '),
        'category_post':category_post
    }
    return render(request,'posts/category.html',context)

# def categorylistview(request):
#     cats_list = Category.objects.all()
#     context = {
       
#         'cats_list':cats_list
#     }
#     return render(request,'posts/category_list.html',context)

