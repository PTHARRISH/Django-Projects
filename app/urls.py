# Create urls.py file in app
from django.urls import path
from . import views

urlspattern=[
    path('\home',views.home,name='home')
]