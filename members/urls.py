from django.urls import path
from .views import (
    user_register,
    user_login,
    user_logout,
    UserEditView,
    PasswordChangeView,
    ShowProfilePageView,
    EditProfilePageView,
    CreateProfilePageView
  
)



app_name = "members"
urlpatterns = [
   path('register/',user_register,name='register'),
   path('login/',user_login,name='login'),
   path('logout/',user_logout, name="logout"),
   path('edit_profile/',UserEditView.as_view(), name="edit_profile"),
   path('password/',PasswordChangeView.as_view(template_name=  'members/change_password.html'),name ='password'),
   path('<int:pk>/profile',ShowProfilePageView.as_view(),name = 'show_profile'),
   path('<int:pk>/edit_profile_page',EditProfilePageView.as_view(),name='edit_profile_page'),
   path('create_profile_page/',CreateProfilePageView.as_view(),name = 'create_profile_page'),
  
]