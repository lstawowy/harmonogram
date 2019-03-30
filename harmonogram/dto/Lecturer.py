from dataclasses import dataclass

from harmonogram.containers.Timetable import Timetable
from harmonogram.rules.LecturerRules import LecturerRules


@dataclass
class Lecturer(object):
    name: str
    timetable: Timetable

    def __init__(self, name, timetable):
        self.name = name
        self.timetable = timetable

    def count_points(self):
        self.timetable.rules = LecturerRules()
        self.timetable.count_all()
