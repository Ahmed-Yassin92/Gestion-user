from operator import index
from django.urls import path

from . import views
from .formulaire import form_log

urlpatterns =[
    path('',views.index, name='index'),
    path('<int:user_id>/detail/', views.detail, name= 'detail'),
    path('/Merci', views.get_name, name='auth' )
]
