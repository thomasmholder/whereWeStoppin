from coordinates import Coordinates
from room import Room


class Person:

    def __init__(self, location, room):
        self.location = Coordinates(0, 0)
        self.preferences = []

    def setlocation(self, coordinates):
        self.location = coordinates

    # def addpreferences(self):