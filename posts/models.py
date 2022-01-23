from calendar import c
from distutils.command.upload import upload
from email.mime import image
import imp
from pyexpat import model
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
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE )
    bio = models.TextField()
    profile_image = models.ImageField(blank = True, null = True, upload_to = 'profile/')
    website_url = models.CharField(max_length=255,blank = True, null = True)
    facebook_url = models.CharField(max_length=255,blank = True, null = True)
    twitter_url= models.CharField(max_length=255,blank = True, null = True)
    instagram_url = models.CharField(max_length=255,blank = True, null = True)
    linkedin_url = models.CharField(max_length=255,blank = True, null = True)
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("posts:home")
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank = True, null = True, upload_to = 'media/')
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
    

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '%s- %s' % (self.post.title,self.name)