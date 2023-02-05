from django import forms

import utils.utils
from roomsession.models import RoomEntry


class JoinRoomForm(forms.Form):
    join_room_id = forms.CharField(label="Join room", max_length=8)


class RoomCreationForm(forms.Form):
    event_type = forms.CharField(label="Where would you like to go",
                                 widget=forms.RadioSelect(choices=RoomEntry.ROOM_TYPES))


class UserCreationForm(forms.Form):
    user_name = forms.CharField(label="Name")
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")
    preferences = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=utils.utils.RESTAURANT_PREFERENCES))
    print(preferences.__str__())
