from django.shortcuts import render, HttpResponse, redirect

def users_home(request):
    return redirect('../blogs/')

def users_login(request):
    return HttpResponse('Placeholder for users to log in')

def users_register(request):
    return HttpResponse('placeholder for users to create a new user record')

def users_index(request):
    return HttpResponse('Placeholder to later display all the list of users')
