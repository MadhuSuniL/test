from django.contrib import admin
from django.urls import path
from users.views import *
urlpatterns = [
    path('',loginpage),
    path('login/',login_user),
    path('logout/',logout_user),
    path('newlogin/',newlogin_user),
    path('home/',home)
]
