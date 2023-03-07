from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Mrng(request):
    return HttpResponse('<h1>Hey....Good Morning</h1>')

def Evng(request):
    return HttpResponse('<marquee><h1>Good Evening Dear!!!!!!!!!!!!!!</h1></marquee>')