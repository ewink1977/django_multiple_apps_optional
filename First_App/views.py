from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse('Placeholder later to display a list of all blogs')

def new(request):
    return HttpResponse('Placeholder to display a new form to create a new blog')

def create(request):
    return HttpResponseRedirect('/')

def show(request, blog):
    return HttpResponse('Placeholder to display blog number: {}'.format(blog))

def edit(request, blog):
    return HttpResponse('Placeholder to edit blog number: {}'.format(blog))

def destroy(request, blog):
    return HttpResponseRedirect('/')