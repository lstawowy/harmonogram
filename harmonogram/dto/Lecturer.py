from dataclasses import dataclass

from harmonogram.containers.Timetable import Timetable
from harmonogram.rules.LecturerRules import LecturerRules


@dataclass
class Lecturer(object):
    name: str
    timetable: Timetable
    lecturer_points: int

    def __init__(self, name, timetable):
        self.name = name
        self.timetable = timetable
        self.lecturer_points = self.count_points()
        print("Lecturer points: " + str(self.lecturer_points))

    def count_points(self):
        self.timetable.rules = LecturerRules()
        self.timetable.count_all()
        return self.timetable.total_points

    def get_timetable(self):
        return self.timetable

    def add_course_to_timetable(self, course):
        return self.timetable.add_course(course)
