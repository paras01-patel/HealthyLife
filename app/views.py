from django.shortcuts import render,redirect
from .models import cont,signn
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.



#home section

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


@never_cache
def sign(req):
    if req.method == "POST":
        username = req.POST.get('username')
        email = req.POST.get('email')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')

        if password1 != password2:
            messages.error(req,"password does not march")
            return render(req,'sign.html')
        
        if signn.objects.filter(username=username).exists():
            messages.error(req, "Username already exists")
            return render(req, 'sign.html')

        user=signn.objects.create(
            username=username,
            email=email,
            password1=password1,
            password2=password2
        )
        req.session['user_id'] = user.id

        messages.success(req, "Account Created Successfully")
        return redirect('userpanel') 

    return render(req, 'sign.html')


@never_cache
def logout(req):
    req.session.pop('user_id', None)   
    return redirect('sign')


#userpanel

@never_cache
def userpanel(req):
    user_id = req.session.get('user_id')
    if not user_id:
        return redirect('sign')
    user = signn.objects.get(id=user_id)
    return render(req, 'userpanel.html', {'user': user})

#adminpanel


@never_cache
def adminpanel(req):
    return render(req,'adminpanel')

