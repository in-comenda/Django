from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    #return HttpResponse('<h1>Alura Space</h1>')
    return render(request, 'galeria/index.html')



# Create your views here.
