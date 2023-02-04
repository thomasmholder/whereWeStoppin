import django.db.models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import roomsession.models
from roomsession.forms import JoinRoomForm, RoomCreationForm

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


def create_room(request):
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            new_room_id = utils.utils.create_room(form.cleaned_data['event_type'])
            return HttpResponseRedirect('/rooms/' + new_room_id)
        else:
            return HttpResponse("Invalid form, somehow")
    else:
        return render(request, "RoomCreation.html", {'room_creation_form': RoomCreationForm})


def join_room(request):
    if request.method == 'POST':
        form = JoinRoomForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/rooms/' + form.cleaned_data['join_room_id'])

    return HttpResponseRedirect('/')


def access_room(request, room_id):
    try:
        trip_type = roomsession.models.RoomEntry.objects.get(room_id=room_id).room_type
    except django.db.models.Model.DoesNotExist:
        trip_type = "None"

    return render(request, "RestaurantPreferences.html", {'room_id': room_id, 'trip_type': trip_type})


def access_room_results(request, room_id):
    try:
        room = roomsession.models.RoomEntry.objects.get(room_id=room_id)
    except django.db.models.Model.DoesNotExist:
        return HttpResponse("Room does not exist")
    if utils.utils.should_compute(room_id):
        lat, long = utils.utils.get_midpoint(room_id)
        room.result_address = utils.utils.da_algorithm(lat, long, "mexican restaurant")
        room.result_number = roomsession.models.UserEntry.objects.all().filter(room=room_id).count()
        room.save()

    return render(request, "Results.html", {'result': room.result_address, 'num_people': str(room.result_number)})
