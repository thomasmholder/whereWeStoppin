import uuid
import textwrap


class Room:


    def __init__(self, eventtype):
        self.id = self.generateid()
        self.eventType = eventtype
        self.users = []

    def generateid(self):
        # Generates 32 bit unique ID and parses the first 8 characters
        return textwrap.shorten(str(uuid.uuid4()), width=8)

    def addnewuser(self, person):
        self.users.append(person)