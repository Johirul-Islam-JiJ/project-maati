from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    context = {"title":"Home | Maati"}
    if request.user.is_seller:
        return render(request, 'seller.html', context)
    if request.user.is_buyer:
        return render(request, 'buyer.html', context)
    if request.user.is_superuser:
        return render(request, 'home.html', context)


def mylogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        email = request.POST.get('email')
        upass = request.POST.get('password')
        # print(email, upass)
        if email != '' and upass != '':
            user = authenticate(email=email, password=upass)
            if user !=  None:
                login(request, user)
                return redirect('/')
        else:
            return redirect('/login')
    context = {"title": "Login | Maati"}
    return render(request, 'login.html', context)

def myregistration(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        address = request.POST.get('address')
        usertype = request.POST.get('usertype')
        if usertype == "buyer":
            user = CustomUser(
                full_name = name,
                email = email,
                address = address,
                is_buyer = True,
                is_active = True
            )
            if password == confirm_password:
                user.set_password(password)
                user.save()
                
        else:
            user = CustomUser(
                full_name = name,
                email = email,
                address = address,
                is_seller = True,
                is_active = True
            )
            if password == confirm_password:
                user.set_password(password)
                user.save()
        return redirect('/login')
        
    context = {"title": "Registration | Maati"}
    return render(request, 'registration.html', context)


def mylogout(request):
    logout(request)
    return redirect('/login')


def profile(request):
    context = {"user": request.user,"title":"Profile | Maati"}
    return render(request, 'profile.html', context)

def post_land_info(request):
    context = {"title":"Post Land Infor | Maati"}
    return render(request, 'post_land.html', context)