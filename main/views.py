from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *
import folium
from folium.map import Tooltip
from django.conf import settings
# Create your views here.

def home(request):
    approved_lands = LandInformation.objects.filter(is_approved=True)
    if not request.user.is_authenticated:
        return redirect('/login')
        
    context = {"title":"Home | Maati","approved_lands": approved_lands[0:4]}
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
                seller = Seller(
                    user = user,
                )
                seller.save()
                
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
                buyer = Buyer(
                    user = user,
                )
                buyer.save()
        return redirect('/login')
        
    context = {"title": "Registration | Maati"}
    return render(request, 'registration.html', context)


def mylogout(request):
    logout(request)
    return redirect('/login')


def profile(request):
    context = {"user": request.user,"title":"Profile | Maati"}
    return render(request, 'profile.html', context)

def lands(request):
    seller = Seller.objects.get(user=request.user)
    lands = SellerLands.objects.select_related().filter(user=seller)
    # landinfo = LandInformation.objects.get

    context = {"title": "Lands | Maati", "lands": lands}
    return render(request, 'lands.html', context)


def post_land_info(request):

    if request.method == "POST":
        land = LandInformation(
            total_area = request.POST["total_area"],
            minimum_price = request.POST["min_price"],
            maximum_price = request.POST["max_price"],
            longitude = request.POST["longitude"],
            latitude = request.POST["latitude"],
            land_image = request.FILES["land_image"],
            is_approved= False
        )
        land.save()

    context = {"title":"Post Land Infor | Maati"}
    return render(request, 'post_land.html', context)


def approve_lands(request):
    if request.method == "POST":
        land = request.POST.get('land')
        LandInformation.objects.filter(pk=land).update(is_approved=True)

    # context
    lands = LandInformation.objects.all()
    context = {"title": "Approve Lands | Maati", "lands": lands}
    return render(request, 'approve_land.html', context)

def all_lands(request):
    lands = LandInformation.objects.all()
    context = {"title" :"All Land Infos | Maati","lands": lands }
    return render(request, "all_lands.html", context)

def get_full_info(request, slug):
    land = LandInformation.objects.get(pk=slug)


    m = folium.Map(location=[land.longitude, land.latitude],tiles="Stamen Terrain", zoom_start=12)

    Tooltip='Click for more info'

    folium.Marker([land.longitude, land.latitude], 
                    popup='<strong>Location One</strong>',
                    tooltip=Tooltip).add_to(m)

    folium.CircleMarker(
        location=[land.longitude, land.latitude],
        radius=50,
        popup='My area',
        color ='#428bca',
        fill = True,
        fill_color ='#428bca'
    ).add_to(m)

    seller = SellerLands.objects.get(pk=land.pk)
    print(seller)


    context = {"title":"Land Info | Maati", "land" : land, "map":m._repr_html_(),"seller": seller}
    return render(request, "land_info.html", context)