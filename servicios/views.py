from django.shortcuts import render
from .models import Servicio

# Create your views here.
def servicios(request):
    servis=Servicio.objects.all()
    return render(request,"servicios/servicios.html",{"servicios":servis})
