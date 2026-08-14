from django.shortcuts import render,redirect
from django.contrib.auth.models import User
import re
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import ProfilePic


# Create your views here.

def valid_pasw(pasw):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    return re.match(pattern,pasw)
    
def register(request):
    if request.method =="POST":
        uname = request.POST['username']
        pasw = request.POST['password']
        cpasw = request.POST['confirm_password']

        try :
            User.objects.get(username = uname)
            messages.error(request,"Name is already defined...!")
            return redirect('register')
        except:
            if pasw != cpasw:
                messages.error(request,'password are not matching...!')
                return redirect('register')

            if not valid_pasw(pasw):
                messages.error(request,'Enter password in A-Z ,a-z,0-9 and must one special character')
                return redirect('register')
            
            user = User.objects.create_user(
                username = uname,
                email = request.POST['email'],
                password = pasw,
                )
            ProfilePic.objects.create(user=user)
            return redirect('login_')
            
            
    return render(request,'register.html')


def login_(request):
    if request.method == "POST":
        uname = request.POST['username']
        pasw = request.POST['password']
        user = authenticate(request,username = uname,password = pasw)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username and password....!')

    return render(request,'login.html')

def update(request):
    profilee = ProfilePic.objects.get(user = request.user)
    if request.method == "POST":
        user = User.objects.get(username = request.user)    
        user.username = request.POST['uname']
        user.email = request.POST['email']
        pic = request.FILES.get('pic')
        user.save()
        if pic:
            profilee.profile = pic
            profilee.save()
        messages.success(request,'success')
        return redirect('profile')
    return render(request,'update.html')

@login_required(login_url='login_')
def profile(request):
    profile, created = ProfilePic.objects.get_or_create(
        user=request.user
    )
    return render(request, "profile.html", {"profile": profile})


def logout_(request):
    logout(request)
    return redirect('login_')