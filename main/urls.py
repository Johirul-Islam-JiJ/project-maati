from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.mylogin,name="login"),
    path('registration/', views.myregistration,name="registration"),
    path('logout/', views.mylogout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('postlands/',views.post_land_info, name="postlands"),
    path('lands/',views.lands, name="lands"),
    path('approve/', views.approve_lands, name="approve"),
    path('all_lands/', views.all_lands, name="landbuy"),
    path('land/<str:slug>', views.get_full_info, name="get_info")
]