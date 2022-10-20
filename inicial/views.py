from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicial(request):
    HttpResponse('<h1>Hello World!</h1>')