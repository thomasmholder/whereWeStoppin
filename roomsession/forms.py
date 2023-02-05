from django import forms

import utils.utils
from roomsession.models import RoomEntry


class JoinRoomForm(forms.Form):
    join_room_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'type code here', 'style': 'width: 400px; background-color: #635956; height:60px; border-radius: 100px; border-color: #635956; border-style:solid; opacity:0.7; padding-bottom: 5px; text-align:center;font-size: 30px;font-weight: 600; font-color:#9D6753;'}),
                                   label="", max_length=8)


class RoomCreationForm(forms.Form):
    event_type = forms.CharField(label="", widget=forms.RadioSelect(choices=RoomEntry.ROOM_TYPES))


class UserCreationForm(forms.Form):
    user_name = forms.CharField(label="Name")
    address = forms.CharField(label="Address")
    preferences = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=utils.utils.RESTAURANT_PREFERENCES))
    print(preferences.__str__())

