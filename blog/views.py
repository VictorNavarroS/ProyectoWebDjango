from django.shortcuts import render
from .models import Categoria, Posteo

# Create your views here.
def blog(request):
    posts=Posteo.objects.all()
    return render(request,"blog/blog.html",{"posteos":posts})
