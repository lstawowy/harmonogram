from dataclasses import dataclass

from ..containers.Timetable import Timetable


@dataclass
class Room(object):
    name: str
    timetable: Timetable
    capacity: int

    def __init__(self, name, timetable, capacity):
        self.name = name
        self.timetable = timetable
        self.capacity = capacity

    def check_is_available(self):
        pass

    def show_harmonogram(self):
        pass
