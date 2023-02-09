from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("I have officially begun messing around :D")

def item(request):
    return HttpResponse("This isn't the index function")
