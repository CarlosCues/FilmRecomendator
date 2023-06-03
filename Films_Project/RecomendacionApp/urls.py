from django.urls import path

from RecomendacionApp import views

urlpatterns=[
    path('',views.index,name='index'),

]