from django.shortcuts import render, HttpResponse
from .models import newboarn
from math import *


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def child(request):
    newboarns = newboarn.objects.all()
    print(newboarns)
    n = len(newboarns)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(nSlides,1),'newboarn': newboarns}
    return render(request, 'meetchildren.html', params)
def donation(request):
    return render(request, 'donation.html')
def adopt(request):
    return render(request, 'adopt.html')
def age_3_5(request):
    return render(request, 'age_3_5.html')
def age_6_10(request):
    return render(request, 'age_6_10.html')
def age_11_15(request):
    return render(request, 'age_11_15.html')
def age_16_18(request):
    return render(request, 'age_16_18.html')
