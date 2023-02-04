from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from roomsession.forms import JoinRoomForm
# Create your views here.
import utils.utils


def landing_page(request, *args, **kwargs):
    return render(request, "Landing.html", {'form': JoinRoomForm()})

def room_creation(*args, **kwargs):
    return HttpResponse("<h1>Room Creation</h1>")

def preferences_selection(*args, **kwargs):
    return HttpResponse("<h1>Preferences Selection</h1>")

def results_page(*args, **kwargs):
    return HttpResponse("<h1>Results!</h1>")


def create_room_post(request):
    return create_room()


def create_room():
    return HttpResponse("Welcome to room creation " + utils.utils.create_room())


def join_room(request):
    if request.method == 'POST':
        form = JoinRoomForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/rooms/'+form.cleaned_data['join_room_id'])

    return HttpResponseRedirect('/')


def access_room(request, room_id):
    return HttpResponse(f"You are in room {room_id}")
