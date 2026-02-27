from django.shortcuts import render,redirect
from .models import cont,signn
from django.contrib import messages

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
def login(req):
    if req.method == "POST":
        username = req.POST.get('username')
        email = req.POST.get('email')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')

        if password1 != password2:
            messages.error(req,"password does not march")
            return render(req,'login.html')
        
        if signn.objects.filter(username=username).exists():
            messages.error(req, "Username already exists")
            return render(req, 'login.html')

        signn.objects.create(
            username=username,
            email=email,
            password1=password1,
            password2=password2
        )

        messages.success(req, "Account Created Successfully")
        return redirect('adminpanel') 

    return render(req, 'login.html')


def adminpanel(req):
    return render(req,'adminpanel.html')