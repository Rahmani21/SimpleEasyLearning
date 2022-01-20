from unicodedata import name
from django.urls import path

from posts.models import Category
from .views import (
   DeletePostView,
   HomeView,
   DetailsVeiw,
   AddPostView,
   UpdatePostView,
   DeletePostView,
   AddCategoryView,
   categoryview,
   
)


app_name = "posts"
urlpatterns = [
   path('',HomeView.as_view(), name='home'),
   path('details/<int:pk>',DetailsVeiw.as_view(), name = 'details'),
   path('add_post/',AddPostView.as_view(),name="add_post"),
   path('add_category/',AddCategoryView.as_view(),name="add_category"),
   path('edit/<int:pk>',UpdatePostView.as_view(), name='edit_post'),
   path('delete/<int:pk>',DeletePostView.as_view(), name='delete_post'),
   path('category/<str:category>',categoryview,name="category"),
   # path('category-list/',categorylistview,name="category-list"),
   
]
