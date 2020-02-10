from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Juego


# Create your views here.

def home(request):
    juegos = Juego.objects
    return render(request, 'home.html',{'data':juegos})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')