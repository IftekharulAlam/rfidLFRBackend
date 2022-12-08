from django.urls import path

from . import views

urlpatterns = [

    path('writelocation', views.writelocation, name='writelocation'),
    path('readlocation', views.readlocation, name='readlocation'),


]
