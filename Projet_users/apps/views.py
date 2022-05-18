from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Users

def index(request):

    list_Users = Users.objects.all()
    template = loader.get_template('apps/index.html')
    context = {
        'list_Users': list_Users,
    }
    return HttpResponse(template.render(context, request))

def Users(request):
    list_Users = Users.objects.all()
    template = loader.get_template('apps/Users.html')
    context = {
        'list_Users': list_Users,
    }
    return HttpResponse(template.render(context, request))

def details (request):
    return HttpResponse('hello you are in the details page')
