from django.urls import path

from . import views

urlpatterns = [

    path('controlCar', views.controlCar, name='controlCar'),
    path('writelocation', views.writelocation, name='writelocation'),
    path('readStatus', views.readStatus, name='readStatus'),




]
