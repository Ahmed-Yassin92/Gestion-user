from operator import index
from django.urls import path

from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('<int:user_id>/detail/', views.detail, name= 'detail'),
    path('register/', views.register, name='register'),
    path('profil/', views.profil, name='profil'),
    path('connexion/',views.connexion,name='connexion')
]
