from dataclasses import dataclass


@dataclass
class Student(object):
    name: str
    timetable: Timetable
    points: int

    def __init__(self, name, timetable):
        self.name = name
        self.timetable = timetable
        self.count_points()

    def count_points(self):
        pass
