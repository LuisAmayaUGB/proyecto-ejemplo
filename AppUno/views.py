from django.shortcuts import render
from django.http import HttpResponse

from .models import Persona
# Create your views here.


def index(request):
    return HttpResponse('Bienvenidos a Django!')


def luis(request):
    return HttpResponse('Bienvenidos a luis!')


def datos(request):
    return HttpResponse('Bienvenidos a Datos!')


def conpag(request):
    psona=Persona.objects.all()
    sintexto = {
        'perso': psona,
        'clase': 'Programación III',
        'Profesor': 'Luis Amaya'
    }
    return render(request, 'index.html', sintexto)


def servicios(request):
    persona=Persona.objects.all()
    contexto={
        'perso':persona
    }
    return render(request,'services.html', contexto)


def about(request):
    return render(request, 'about.html')


