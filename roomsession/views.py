from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")

def room_creation(*args, **kwargs):
    return HttpResponse("<h1>Room Creation</h1>")

def preferences_selection(*args, **kwargs):
    return HttpResponse("<h1>Preferences Selection</h1>")

def results_page(*args, **kwargs):
    return HttpResponse("<h1>Results!</h1>")
