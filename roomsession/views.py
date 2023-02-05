import django.db.models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import roomsession.models
from roomsession.forms import JoinRoomForm, RoomCreationForm, UserCreationForm

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            utils.utils.create_user_entry(room_id, form.cleaned_data['user_name'], form.cleaned_data['address'],
                                          form.cleaned_data['preferences'])
            return HttpResponseRedirect(f"{room_id}/results")
    else:
        try:
            trip_type = roomsession.models.RoomEntry.objects.get(room_id=room_id).room_type
        except django.db.models.Model.DoesNotExist:
            return HttpResponse("Room does not exist")

        if trip_type == "RS":
            return render(request, "RestaurantPreferences.html", {'user_creation_form': UserCreationForm,
                                                                  'room_id': room_id})
        else:
            return HttpResponse("Invalid trip type")


def access_room_results(request, room_id):
    try:
        room = roomsession.models.RoomEntry.objects.get(room_id=room_id)
    except django.db.models.Model.DoesNotExist:
        return HttpResponse("Room does not exist")
    if utils.utils.should_compute(room_id):
        ideal_location = utils.utils.get_ideal_location_type(room_id)
        lat, long = utils.utils.get_midpoint(room_id)
        room.result_address = utils.utils.da_algorithm(lat, long, ideal_location)
        room.result_number = roomsession.models.UserEntry.objects.all().filter(room=room_id).count()

        # Map fetch goes here

        room.save()

    return render(request, "Results.html", {'result': room.result_address, 'num_people': str(room.result_number)})
