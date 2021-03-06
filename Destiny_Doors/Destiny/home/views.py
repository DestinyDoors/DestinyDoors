from email import message
from email.headerregistry import Address
from email.message import Message
from pyexpat.errors import messages
from ssl import Purpose
from unicodedata import category
from django.shortcuts import render, HttpResponse , redirect
from .models import   winterdonation,parent_adopted_form,booking_table,donateanything, newboarn, age_3_5y, age_6_10y, age_11_15y, age_16_18y
#from .models import contactme
from django.contrib.auth import authenticate, login , logout
from home.models import moneydonate  
from math import *
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


def sign_up(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,user + ' , Thank for registration')
            return redirect('/log_in')
    context = {'form':form}
    return render(request,'signup.html', context)

def log_in(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/partners')
        else:
            messages.info(request, 'Username Or Password is Incorrect')
    context = {}
    return render(request,'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')
#@login_required(login_url='/index')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def partners(request):
    Partner_list =booking_table.objects.all()
    params = {'Partner_list':Partner_list}
    return render(request, 'partners.html', params)

def payment(request):
    return render(request, 'paymentdone.html')

def moneyd(request):

    return render(request, 'moneyd.html')

'''
def partner(request):
    if request.method=='POST':
        Organization = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Purpose = request.POST.get('purpose')
        Date = request.POST.get('date')

        DP=partnerreg(Organization=Organization,Email=Email,Phone=Phone,Purpose=Purpose,Date=Date)
    return render(request, 'partner.html')
'''

def booking(request):
       
    if request.method=='POST':
        org_name = request.POST.get('name')
        email = request.POST.get('email')
        purpose = request.POST.get('purpose')
        date = request.POST.get('date')
        book = booking_table(Name=org_name,Email=email,Purpose=purpose,Date=date)
        book.save()  
    return render(request, 'booking.html')

def donationdone(request):
    
    return render(request, 'donationdone.html')

def summerdonation(request):
    
    return render(request, 'summer_campaign.html')

def Mdonation(request):
    if request.method=='POST':
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cardno = request.POST.get('cardno')
        exp = request.POST.get('exp')
        cvv = request.POST.get('cvv')

        Data=moneydonate(Name=first_name,Email_Id=email,Phone=phone,Card_no=cardno,Exp=exp,Cvv=cvv)
        
        Data.save()
    return render(request, 'Money_Donate.html')

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
'''
def money_c(request):
    if request.method=='POST':
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        donatebox = request.POST.get('donatebox')
        Dm=givemoney(Name=first_name,Email_Id=email,Phone=phone,City=city,State=state,Pin=pin,Donatebox=donatebox)
       
        Dm.save() 
        
    return render(request, 'moneyd.html')
    '''
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
    

def adopt(request):
    if request.method=='POST':
        name = request.POST.get('aname')
        dob = request.POST.get('dob')
        aadhar = request.POST.get('aadhar')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        bchilds = request.POST.get('bchild')
        achilds = request.POST.get('achild')
        address = request.POST.get('address')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pin = request.POST.get('pincode')
        parent_Data = parent_adopted_form(Name=name,DOB=dob,Aadhar=aadhar,Email=email,Phone=phone,
        Biological_Childrens=bchilds,Adopted_Children=achilds,Address=address,District=district,
        State=state,Pincode=pin)
        parent_Data.save()

        
  
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



