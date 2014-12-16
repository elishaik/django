from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse(r"Rango say hello world! <br/> <a href ='" + r"/rango/about'" +r">About</a>")

def about(request):
    return HttpResponse(r"Rango says here is the about page <br/> <a href ='" + r"/rango'" +r">Index</a>")