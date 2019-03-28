from dataclasses import dataclass


@dataclass
class Lecturer(object):
    name: str
    timetable: Timetable

    def __init__(self, name, timetable):
        self.name = name
        self.timetable = timetable
