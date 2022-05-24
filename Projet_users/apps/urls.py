from operator import index
from django.urls import path

from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('<int:user_id>/detail/', views.detail, name= 'detail'),
    path('inscription/', views.inscription, name='inscription'),
    path('profil/', views.profil, name='profil'),
    path('connexion/',views.connexion,name='connexion')
]
