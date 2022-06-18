from django.shortcuts import render, HttpResponse
from .models import newboarn,age_3_5y,age_6_10y,age_11_15y,age_16_18y
from math import *


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def donation(request):
    return render(request, 'donation.html')
def step(request):
    return render(request, 'step_parents.html')
def story(request):
        return render(request, 'story.html')
def child(request):
    newboarns = newboarn.objects.all()
    n = len(newboarns)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(nSlides,1),'newboarn': newboarns}
    return render(request, 'meetchildren.html', params)
def adopt(request):
    return render(request, 'adopt.html')
def age_3_5(request):
    age_3_5ys = age_3_5y.objects.all()
    n = len(age_3_5ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(nSlides,1),'age_3_5y': age_3_5ys}
    return render(request, 'age_3_5.html', params)
def age_6_10(request):
    age_6_10ys = age_6_10y.objects.all()

    n = len(age_6_10ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(nSlides,1),'age_6_10y': age_6_10ys}
    return render(request, 'age_6_10.html', params)
def age_11_15(request):
    age_11_15ys = age_11_15y.objects.all()
    
    n = len(age_11_15ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(nSlides,1),'age_11_15y': age_11_15ys}
    return render(request, 'age_11_15.html', params)
def age_16_18(request):
    age_16_18ys = age_16_18y.objects.all()
    
    n = len(age_16_18ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(nSlides,1),'age_16_18y': age_16_18ys}
    return render(request, 'age_16_18.html', params)



def child_data(request, myid):
    #fetch product by id
    newboarns = newboarn.objects.filter(id=myid)
    print(newboarns)
    return render(request, 'childviewsite.html', {'newboarn':newboarns[0]})

def age_3_5yr(request, myid):
    #fetch product by id
    age_3_5ys = age_3_5y.objects.filter(id=myid)
    print(age_3_5ys)
    return render(request, 'age_3_5_viewsite.html', {'age_3_5y':age_3_5ys[0]})

def age_6_10yr(request, myid):
    #fetch product by id
    age_6_10ys = age_6_10y.objects.filter(id=myid)
    print(age_6_10ys)
    return render(request, 'age_6_10_viewsite.html', {'age_6_10y':age_6_10ys[0]})

def age_11_15yr(request, myid):
    #fetch product by id
    age_11_15ys = age_11_15y.objects.filter(id=myid)
    print(age_11_15ys)
    return render(request, 'age_11_15_viewsite.html', {'age_11_15y':age_11_15ys[0]})

def age_16_18yr(request, myid):
    #fetch product by id
    age_16_18ys = age_16_18y.objects.filter(id=myid)
    print(age_16_18ys)
    return render(request, 'age_16_18_viewsite.html', {'age_16_18y':age_16_18ys[0]})

