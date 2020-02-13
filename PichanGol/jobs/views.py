from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Juego, Cancha, Jugador
from datetime import date, datetime, timedelta


# Create your views here.

def home(request):
    startdate = datetime.today()
    enddate = startdate + timedelta(days=1)
    juegos = Juego.objects.filter(fecha__range=[startdate, enddate])
    return render(request, 'home.html',{'data':juegos})

def listajuegos(request):
    listajuegos = Juego.objects
    return render(request, 'listajuegos.html',{'data':listajuegos})

def detail(request,juego_id):
    listacanchas= Cancha.objects
    juego_detail = get_object_or_404(Juego,pk=juego_id)
    return render(request,'juego.html',{'data':juego_detail})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

