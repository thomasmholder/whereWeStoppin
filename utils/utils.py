import textwrap

import roomsession.models as models
import uuid


def create_room() -> str:
    new_room_id = textwrap.shorten(str(uuid.uuid4()), width=8)
    if not models.RoomEntry.objects.filter(room_id=new_room_id):
        new_room_entry = models.RoomEntry(room_id=new_room_id)
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
