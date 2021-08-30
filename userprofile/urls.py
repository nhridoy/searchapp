from django.urls import path
from userprofile import views

app_name = 'profileapp'

urlpatterns = [
    path('', views.userProfileView, name='profile'),
    path('edit_profile/', views.editProfileView, name='edit-profile'),
    path('change_password/', views.changePassView, name='change-password'),
    path('logout/', views.logoutView, name='logout'),
    path('login/', views.loginView, name='login'),
    path('registration/', views.registrationView, name='register'),
]