from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('contact', views.contact_page_view, name= 'contact'),
    path('about', views.about_page_view, name='about')
]