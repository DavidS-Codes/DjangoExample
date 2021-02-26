from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
    if request.method == 'POST':
        usuario = request.POST["usuario"]
        contrasena = request.POST["contrasena"]
        user = authenticate(username=usuario, password=contrasena)
        if user is not None:
            print("El usuario existe en la base de datos")
        else:
            print("El usuario no existe en la base de datos")
            
        return render(request, 'index.html')
    else:    
        return render(request, 'index.html')