from django.shortcuts import render, HttpResponse
from data1.models import Actualizacion

# Create your views here.

def casa(request):
    actualizacion = Actualizacion.objects.all()
    return render(request,"monitor/casa.html",{'actualizacion': actualizacion})

def auto(request):
    actualizacion = Actualizacion.objects.all()
    return render(request,"monitor/auto.html",{'actualizacion': actualizacion})

def indec(request):
    return render(request,"monitor/indec.html")

def contacto(request):
    return render(request,"monitor/contacto.html")




