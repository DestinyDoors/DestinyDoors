from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('adopt', views.adopt, name='donation'),
    path('contact', views.contact, name='contact'),
    path('child', views.child, name='child'),
    path('donation', views.donation, name='donation'),
]
