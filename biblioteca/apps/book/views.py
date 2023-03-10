from django.shortcuts import render

from .models import Author2
# Create your views here.


def book(request):
    autor2_listar = Author2.objects.all()
    return render(request,'book/inicio.html',{'book':autor2_listar})