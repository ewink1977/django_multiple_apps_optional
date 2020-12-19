from django.urls import path
from . import views

urlpatterns = [
    path('', views.surveyhome),
    path('new/', views.surveynew),
]