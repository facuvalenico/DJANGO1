from django.shortcuts import render
from .models import Actualizacion

# Create your views here.

def index(request):
    actualizacion = Actualizacion.objects.all()
    return render(request,"data1/index.html",{'actualizacion': actualizacion})



