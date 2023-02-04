from django import forms


class JoinRoomForm(forms.Form):
    join_room_id = forms.CharField(label="Join room", max_length=8)
