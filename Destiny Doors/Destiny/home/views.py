from email import message
from email.message import Message
from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse
from .models import   winterdonation,sign_up,summerdonation,donateanything, moneydonate, newboarn, age_3_5y, age_6_10y, age_11_15y, age_16_18y
#from .models import contactme
from math import *
from django.core.mail import send_mail



# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def payment(request):
    return render(request, 'paymentdone.html')

def moneyd(request):

    return render(request, 'moneyd.html')

def partner(request):
    
    return render(request, 'partner.html')

def donationdone(request):
    
    return render(request, 'donationdone.html')

def summerd(request):
    if request.method=='POST':
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        donatebox = request.POST.get('donatebox')
        DS=summerdonation(Name=first_name,Email_Id=email,Phone=phone,City=city,State=state,Pin=pin,Donatebox=donatebox)
       
        DS.save()  
    return render(request, 'summer_campaign.html')

def winterd(request):
    if request.method=='POST':
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        donatebox = request.POST.get('donatebox')
        DW=winterdonation(Name=first_name,Email_Id=email,Phone=phone,City=city,State=state,Pin=pin,Donatebox=donatebox)
       
        DW.save()   
    return render(request, 'winter_campaign.html')


def contact(request):
    '''  
    if request.method=='POST':
        first_name = request.POST.get('entry.961833090')
        last_name = request.POST.get('entry.766710902')
        email = request.POST.get('entry.626623658')
        phone = request.POST.get('entry.1165961989')
        message = request.POST.get('entry.1239058374')
        DB=contactme(First_name=first_name,Last_name=last_name,Email_Id=email,Phone=phone,Message=message)
        DB.save()
        '''
    return render(request, 'contact.html')
def donation(request):

    return render(request, 'donation.html')

def money_c(request):
    if request.method=='POST':
        first_name = request.POST.get('cardname')
        email = request.POST.get('emailname')
        phone = request.POST.get('phonename')
        amount = request.POST.get('amt')
        DBB=moneydonate(Name=first_name,Email_Id=email,Phone=phone,Amount=amount)
        
        DBB.save()
        
    return render(request, 'moneyd.html')
    
def one_donate(request):
    if request.method=='POST':
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        donatebox = request.POST.get('donatebox')
        D=donateanything(Name=first_name,Email_Id=email,Phone=phone,City=city,State=state,Pin=pin,Donatebox=donatebox)
       
        D.save()
    return render(request, 'onedonate.html')

def step(request):
    return render(request, 'step_parents.html')


def story(request):
    return render(request, 'story.html')


def child(request):
    newboarns = newboarn.objects.all()
    n = len(newboarns)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        nSlides, 1), 'newboarn': newboarns}
    return render(request, 'meetchildren.html', params)


def adopt(request):
    return render(request, 'adopt.html')


def age_3_5(request):
    age_3_5ys = age_3_5y.objects.all()
    n = len(age_3_5ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        nSlides, 1), 'age_3_5y': age_3_5ys}
    return render(request, 'age_3_5.html', params)


def age_6_10(request):
    age_6_10ys = age_6_10y.objects.all()

    n = len(age_6_10ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        nSlides, 1), 'age_6_10y': age_6_10ys}
    return render(request, 'age_6_10.html', params)


def age_11_15(request):
    age_11_15ys = age_11_15y.objects.all()

    n = len(age_11_15ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        nSlides, 1), 'age_11_15y': age_11_15ys}
    return render(request, 'age_11_15.html', params)


def age_16_18(request):
    age_16_18ys = age_16_18y.objects.all()

    n = len(age_16_18ys)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        nSlides, 1), 'age_16_18y': age_16_18ys}
    return render(request, 'age_16_18.html', params)


def child_data(request, myid):
    # fetch product by id
    newboarns = newboarn.objects.filter(id=myid)
    print(newboarns)
    return render(request, 'childviewsite.html', {'newboarn': newboarns[0]})


def age_3_5yr(request, myid):
    # fetch product by id
    age_3_5ys = age_3_5y.objects.filter(id=myid)
    print(age_3_5ys)
    return render(request, 'age_3_5_viewsite.html', {'age_3_5y': age_3_5ys[0]})


def age_6_10yr(request, myid):
    # fetch product by id
    age_6_10ys = age_6_10y.objects.filter(id=myid)
    print(age_6_10ys)
    return render(request, 'age_6_10_viewsite.html', {'age_6_10y': age_6_10ys[0]})


def age_11_15yr(request, myid):
    # fetch product by id
    age_11_15ys = age_11_15y.objects.filter(id=myid)
    print(age_11_15ys)
    return render(request, 'age_11_15_viewsite.html', {'age_11_15y': age_11_15ys[0]})


def age_16_18yr(request, myid):
    # fetch product by id
    age_16_18ys = age_16_18y.objects.filter(id=myid)
    print(age_16_18ys)
    return render(request, 'age_16_18_viewsite.html', {'age_16_18y': age_16_18ys[0]})


def signup(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        DSU=sign_up(Name=name,Email_Id=email,Password=password,Cpassword=password2)
        DSU.save()
    return render(request, 'onedonate.html')