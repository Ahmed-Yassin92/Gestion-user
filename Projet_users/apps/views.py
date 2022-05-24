from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import User, Sessions
from .forms import FormConnexion, FormInscription
from django import forms


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

def inscription(request):
    form = forms.FormInscription()
    message = ""
    if request.method == 'POST':
        forminscription = FormInscription
        user = User.objects
        return HttpResponse("voici la page d'inscription")
    else:
        return render(request, 'apps/inscription.html')       

def profil(request):
    if request.method == 'POST':
        user = User.objects.get(request.post)
        return HttpResponse("felicitation profil enregistré %s" %user)

def connexion(request):
    context={
         'form':'',
        'message':'Bienvenue dans la page de connexion'
    }
    if request.method =="POST":
        form =FormConnexion(request.POST)
        if form.is_valid():
            
            utilisateur = User.objects.get(email=form.cleaned_data['email'])
          
            if(User.password == form.cleaned_data['password']):
                url = "/"+str(User.iduser) + "/profil/"
                return HttpResponseRedirect(url)
    else:
        form=FormConnexion()
        context={
            'form':form,
            'message':'Bienvenue dans la page de connexion'
        }

