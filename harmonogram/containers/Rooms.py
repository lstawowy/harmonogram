from dataclasses import dataclass


@dataclass
class Rooms(object):
    rooms: list

    def __init__(self, rooms):
        self.rooms = rooms

    def check_is_available(self, start_time, end_time, capacity):
        for room in self.rooms:
            if room.check_is_available(start_time, end_time, capacity):
                return room
