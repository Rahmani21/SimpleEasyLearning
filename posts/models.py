from calendar import c
import imp
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("posts:details", args=(str(self.id)))
        return reverse("posts:home")

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # description = models.TextField()
    description = RichTextField(blank = True,null =True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default='django')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User,related_name='blog_posts')
    def __str__(self):
        return str(self.id) + " | " + self.title + " | " + str(self.author)

    def get_absolute_url(self):
        # return reverse("posts:details", args=(str(self.id)))
        return reverse("posts:home")
    