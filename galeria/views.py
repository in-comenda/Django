from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    #return HttpResponse('<h1>Alura Space</h1>')
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'geleria/imagem.html')



# Create your views here.
