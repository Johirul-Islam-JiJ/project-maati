from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

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


def mylogout(request):
    logout(request)
    return redirect('/login')


def profile(request):
    context = {"user": request.user,"title":"Profile | Maati"}
    return render(request, 'profile.html', context)