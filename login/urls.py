from django.urls import path
from .views import *
app_name = "login"
urlpatterns = [
    path('loginpage/', login_view,name='userlogin'),
]