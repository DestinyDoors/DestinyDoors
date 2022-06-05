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
    path('age_3_5', views.age_3_5, name='age_3_5'),
    path('age_6_10', views.age_6_10, name='age_6_10'),
    path('age_11_15', views.age_11_15, name='age_11_15'),
    path('age_16_18', views.age_16_18, name='age_16_18'),

]
