from operator import index
from django.urls import path

from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('detail/', views.details, name= 'details'),
    path('apps/',views.index, name='apps')
]
