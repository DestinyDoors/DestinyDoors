from email import message
from email.message import Message
from pyexpat.errors import messages
from ssl import Purpose
from unicodedata import category
from django.shortcuts import render, HttpResponse , redirect
from .models import   adoptform,partnerreg,winterdonation,donateanything, givemoney, newboarn, age_3_5y, age_6_10y, age_11_15y, age_16_18y
#from .models import contactme
from django.contrib.auth import authenticate, login
from home.models import moneydonate  
from math import *
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == "POST":
     fm = UserCreationForm(request.POST)
     if fm.is_valid():
        fm.save()
    else:
        fm = UserCreationForm()
    return render(request,'signup.html',{'form':fm})


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

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
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']


        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()

        return redirect('/')

    else:
       return render(request, 'partner.html')

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/about")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/contact")

    return HttpResponse("404- Not found")

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
        Aname=request.POST.get('Aname')
        dob=request.POST.get('dob')
        Gender=request.POST.get('gender')
        Category=request.POST.get('Category')
        id=request.POST.get('id')
        idno=request.POST.get('idno')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        martialstat=request.POST.get('martialstat')

        name1=request.POST.get('name1')
        dob1=request.POST.get('dob1')
        gender1=request.POST.get('gender1')
        Category1=request.POST.get('Category1')
        id1=request.POST.get('id1')
        idno1=request.POST.get('idno1')

        email1=request.POST.get('email1')
        phone1=request.POST.get('phone1')
        bchild=request.POST.get('bchild')
        achild=request.POST.get('achild')

        address=request.POST.get('address')
        district=request.POST.get('district')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')

        address1=request.POST.get('address1')
        district2=request.POST.get('district2')
        state2=request.POST.get('state2')
        pincode2=request.POST.get('pincode2')
        D=adoptform(Applicant_Name=Aname,Date_of_Birth=dob,Gender=Gender,Category=Category,Document=id,ID_NO=idno,
        Email_ID=email,Phone=phone,Martital_Status=martialstat,Spouse_name=name1,Spouse_DOB=dob1,Spouse_Gender=gender1,
        Spouse_Category=Category1,Spouse_Document=id1,Spouse_ID_NO=idno1,Spouse_Email_ID=email1,Spouse_Phone=phone1,
        Biological_children=bchild,Adopted_children=achild,Address=address,District=district,State=state,Pin_code=pincode,
        Current_Address=address1,Current_District=district2,Current_State=state2,Current_Pin_code=pincode2)


    if request.method=='POST':
        Email_login=request.POST.get('emaillog')
        Password_login=request.POST.get('passlog')

        user = authenticate(username=Email_login, password=Password_login)
        
        if user is not None:
            login(request, user)
            Aname = user.Aname
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/adopt.html",{"Aname":Aname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

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



