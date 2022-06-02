from django.shortcuts import render, HttpResponse
from .models import agegroup
from math import *


# Create your views here.
def index(request):
    Agegroups = agegroup.objects.all()
    print(Agegroups)
    n=len(agegroup)
    slide = n//4 + ceil((n/4)-n//4)
    params = {'no_of_slides': slide, 'range':range(1,slide), 'agegroup': Agegroups}
    return render(request, 'index.html', params)


def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def child(request):
    return render(request, 'meetchildren.html')
def donation(request):
    return render(request, 'donation.html')
def adopt(request):
    return render(request, 'adopt.html')
