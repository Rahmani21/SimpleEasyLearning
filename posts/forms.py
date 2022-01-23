from dataclasses import fields
from pyexpat import model
from random import choice
from tkinter import Widget
from django import forms
from .models import Comment, Post,Category

# cats = [
#     ('coding','coding'),
#     ('sports','sports'),
#     ('Math','Math'),
# ]
cats = Category.objects.all().values_list('name','name')

choice_list = []

for item in cats:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','description','snippet','image')
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'','id':'userid','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
            

        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','description','snippet')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
        }



# Create form for Comments 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','description')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),  
        }


