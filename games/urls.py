from django.urls import path
from .views import *
app_name = "games"
urlpatterns = [
    path('home/', homepage,name="home"),
]