from django.contrib import admin

# Register your models here.
from roomsession.models import RoomEntry, UserEntry

admin.site.register(RoomEntry)
admin.site.register(UserEntry)
