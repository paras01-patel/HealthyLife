from django.shortcuts import render
from .models import cont

# Create your views here.


def home(req):
    return render(req,'home.html')


def recipes(req):
    return render(req,'recipes.html')

def bmi(req):
    return render(req,'bmi.html')

def contact(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        subject=req.POST.get('subject')
        message=req.POST.get('message')
        cont.objects.create(name=name,email=email,subject=subject,message=message)      
        
        
    return render(req,'contact.html')


def adminpanel(req):
    return render(req,'adminpanel.html')