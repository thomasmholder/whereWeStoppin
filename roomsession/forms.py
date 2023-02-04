from django import forms
from models import RoomEntry


class JoinRoomForm(forms.Form):
    join_room_id = forms.CharField(label="Join room", max_length=8)


class RoomCreationForm(forms.Form):
    event_type = forms.CharField(label="Where would you like to go",
                                 widget=forms.RadioSelect(choices=RoomEntry.ROOM_TYPES))
