from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import dates
from django.template import loader

from .models import users

def index(request):
    list_users = users.objects.all()
    template = loader.get_template('apps/index.html')
    context = {
        'list_users': list_users,
    }
    return HttpResponse("Bienvenue monsieur %s" %list_users.noms)

def users(request):
    list_users = users.objects.all()
    template = loader.get_template('apps/users.html')
    context = {
        'list_users': list_users,
    }
    return HttpResponse(template.render(context, request))

def details (request):
    return HttpResponse('hello you are in the details page')
