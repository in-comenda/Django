from django.shortcuts import render
from rest_framework import viewsets
from usuarios.forms import LoginForms



def login(request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    return render(request, "usuarios/cadastro.html")





# Create your views here.
