import googlemaps
from datetime import datetime
import django.db.models

import roomsession.models as models
import uuid

# RESTAURANT_PREFERENCES = ['American', 'Mexican', 'Chinese', 'Italian', 'Thai',
#                          'Pizza', 'Indian', 'Korean', 'Japanese', 'Fast Food']

RESTAURANT_PREFERENCES = [
    ("AM", "American"),
    ("MX", "Mexican"),
    ("CH", "Chinese"),
    ("TH", "Thai"),
    ("IN", "Indian"),
    ("FF", "Fast Food"),
    ("IT", "Italian"),
    ("PI", "Pizza"),
    ("AF", "African"),
    ("KR", "Korean"),
    ("JP", "Japanese")
]


def create_room(room_type: str = None) -> str:
    new_room_id = str(uuid.uuid4())[0:8]
    print(models.RoomEntry.objects.filter(room_id=new_room_id))
    if not models.RoomEntry.objects.filter(room_id=new_room_id):
        new_room_entry = models.RoomEntry(room_id=new_room_id, result_number=0, room_type=room_type)
        new_room_entry.save()
        return new_room_id
    else:
        return create_room()


def create_user_entry(room_id: str, user_name: str, user_address: str,
                      user_preferences: str) -> None:
    user_latitude, user_longitude = get_position(user_address)
    user_room = models.RoomEntry.objects.get(room_id=room_id)
    new_user = models.UserEntry(room=user_room, name=user_name, latitude=user_latitude, longitude=user_longitude,
                                preference_list=user_preferences)
    new_user.save()
    user_room.save()


def should_compute(room_id: str) -> bool:
    try:
        room = models.RoomEntry.objects.all().filter(room_id=room_id)[0]
    except django.db.models.Model.DoesNotExist:
        return False

    try:
        people = models.UserEntry.objects.filter(room_id=room_id)
    except models.UserEntry.DoesNotExist:
        return False

    if people.count() == 0:
        return False

    if people.count() == room.result_number:
        return False

    return True


def get_midpoint(room_id: str) -> (float, float):
    if not should_compute(room_id):
        return 0.0, 0.0
    latitudes = []
    longitudes = []

    people = models.UserEntry.objects.all().filter(room=room_id)

    for person in people:
        latitudes.append(person.latitude)
        longitudes.append(person.longitude)

    midpoint_lat = ((max(latitudes) - min(latitudes)) / 2) + min(latitudes)
    midpoint_long = ((max(longitudes) - min(longitudes)) / 2) + min(longitudes)

    return midpoint_lat, midpoint_long


def get_ideal_location_type(room_id: str) -> str:
    try:
        people = models.UserEntry.objects.all().filter(room_id=room_id)
    except models.UserEntry.DoesNotExist:
        return ""

    prefs_list = ""

    for person in people:
        prefs_list += person.preference_list

    prefs_dict = {}
    for pref in RESTAURANT_PREFERENCES:
        prefs_dict[pref[0]] = prefs_list.count(pref[0])

    ideal_pref = max(prefs_dict)
    ideal_loc = " restaurant"
    for i in RESTAURANT_PREFERENCES:
        if i[0] == ideal_pref:
            ideal_loc = i[1] + ideal_loc

    return ideal_loc


def da_algorithm(latitude: float, longitude: float, location_type: str) -> str:
    gmaps = googlemaps.Client(key='AIzaSyCt1LvRCpDQAdK_J3hwse0QRzLv8UCqlL4')

    response = gmaps.places_nearby(
        location=(latitude, longitude),
        keyword=location_type,
        rank_by="distance"
    )

    try:
        return response['results'][0]['name']
    except IndexError:
        return "No suitable location found"


def get_position(address: str) -> (float, float):
    gmaps = googlemaps.Client(key='AIzaSyCt1LvRCpDQAdK_J3hwse0QRzLv8UCqlL4')

    response = gmaps.geocode(address)

    return response[0]['geometry']['location']['lat'], response[0]['geometry']['location']['lng']
