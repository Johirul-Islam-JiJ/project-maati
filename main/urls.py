from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.mylogin,name="login"),
    path('logout/', views.mylogout, name="logout"),
    path('profile/', views.profile, name="profile")
]