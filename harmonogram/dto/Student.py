from dataclasses import dataclass

from ..containers.Timetable import Timetable
from ..rules.StudentRules import StudentRules


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
        self.timetable.rules = StudentRules()
        self.timetable.count_all()
