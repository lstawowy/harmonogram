from dataclasses import dataclass


@dataclass
class Rooms(object):
    rooms: list

    def __init__(self, rooms):
        self.rooms = rooms

    def check_is_available(self):
        pass

    def show_harmonogram(self):
        pass
