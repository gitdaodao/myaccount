from django.urls import path
from .views import *

app_name='account'

urlpatterns=[
    path('dashboard/',dashboard,name='dashboard'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',user_reg,name='register'),
]
