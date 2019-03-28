from dataclasses import dataclass


@dataclass
class Room(object):
    name: str
    timetable: Timetable
    capacity: int

    def __init__(self, name, timetable, capacity):
        self.name = name
        self.timetable = timetable
        self.capacity = capacity
