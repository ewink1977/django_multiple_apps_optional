from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_home),
    path('register', views.users_register),
    path('login', views.users_login),
    path('users/new', views.users_register),
    path('users', views.users_index),
]