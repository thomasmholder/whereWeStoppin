from django.db import models


# Create your models here.
class RoomEntry(models.Model):
    ROOM_TYPES = [
        ('RS', 'Restaurant')
    ]
    room_id = models.CharField(max_length=8, primary_key=True)
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)
    result_number = models.IntegerField(default=0)
    result_address = models.TextField(null=True)


class UserEntry(models.Model):
    room = models.ForeignKey(RoomEntry, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    preference_list = models.TextField()

