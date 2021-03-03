from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('politician_list', views.politician_list, name='politician_list'),
    path('parties_list', views.parties_list, name='parties_list'),
    path('<str:slug>', views.promises, name='promises'),
    path('party/<str:slug>', views.party, name='party'),
    path('politician/<str:slug>', views.politician, name='politician'),
    
]