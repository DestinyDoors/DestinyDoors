from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
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
