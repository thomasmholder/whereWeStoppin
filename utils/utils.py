import googlemaps
from datetime import datetime
import django.db.models

import roomsession.models as models
import uuid

RESTAURANT_PREFERENCES = ['American', 'Mexican', 'Chinese', 'Italian', 'Thai',
                          'Pizza', 'Indian', 'Korean', 'Japanese', 'Fast Food']

def create_room(room_type: str = None) -> str:
    new_room_id = str(uuid.uuid4())[0:8]
    print(models.RoomEntry.objects.filter(room_id=new_room_id))
    if not models.RoomEntry.objects.filter(room_id=new_room_id):
        new_room_entry = models.RoomEntry(room_id=new_room_id, result_number=0, room_type=room_type)
        new_room_entry.save()
        return new_room_id
    else:
        return create_room()


def create_user_entry(room_id: str, user_name: str, user_latitude: float, user_longitude: float,
                      user_preferences: str) -> None:
    new_user = models.UserEntry(room=room_id, name=user_name, latitude=user_latitude, longitude=user_longitude,
                                preference_list=user_preferences)
    new_user.save()
    user_room = models.RoomEntry.objects.get(room_id=room_id)
    user_room.result_number += 1
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

    midpoint_lat = ((max(latitudes) - min(latitudes))/2) + min(latitudes)
    midpoint_long = ((max(longitudes) - min(longitudes))/2) + min(longitudes)

    return midpoint_lat, midpoint_long


def da_algorithm(latitude: float, longitude: float, location_type: str) -> dict:
    gmaps = googlemaps.Client(key='AIzaSyBkggWLN5cIFpGJ1IjNSuw7oKUHfo1U5HY')

    response = gmaps.places_nearby(
        location=(latitude, longitude),
        keyword=location_type,
        rank_by="distance"
    )

    return response['results'][0]['name']