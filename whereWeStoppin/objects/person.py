from coordinates import Coordinates
from room import Room


class Person:
    location = Coordinates(0, 0)
    preferences = []
    room = Room()

    def __init__(self, location, room):
        self.location = location
        self.room = room

    def setlocation(self, coordinates):
        self.location = coordinates

    # def addpreferences(self):