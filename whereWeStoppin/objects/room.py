import uuid
import textwrap


class Room:
    id = ""
    users = []
    eventType = ""

    def __init__(self, eventtype):
        self.generateid()
        self.eventType = eventtype

    def generateid(self):
        # Generates 32 bit unique ID and parses the first 8 characters
        self.id = textwrap.shorten(str(uuid.uuid4()), width=8)
