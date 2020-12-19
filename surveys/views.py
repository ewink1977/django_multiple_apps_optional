from django.shortcuts import render, HttpResponse

def surveyhome(request):
    return HttpResponse('Placeholder to display all the surveys created.')

def surveynew(request):
    return HttpResponse('Placeholder for users to add a new survey!')


