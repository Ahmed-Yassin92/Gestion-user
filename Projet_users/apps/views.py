from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from psutil import users

from .models import User, Sessions



def index (request):
    list_users = User.objects.all()
    template = loader.get_template('apps/index.html')
    context = {
        'list_users': list_users,
    }
    return HttpResponse(template.render(context, request))

def Users(request):
    list_users = User.objects.all()
    template = loader.get_template('apps/Users.html')
    context = {
        'list_users': list_users,
    }
    return HttpResponse(template.render(context, request))

def sessions(request):
    list_sessions = Sessions.objects.all()
    template = loader.get_template('main_app/sessions.html')
    context = {
        'list_sessions': list_sessions,
    }
    return HttpResponse(template.render(context, request))

def detail (request, user_id):
    users= User.objects.get(pk=user_id)
    # list_sessions = user.sessions_set.all
    return render(request, 'apps/detail.html', {'users': users})
   # return HttpResponse('hello you are in the details page %s ' % user_id)
    
