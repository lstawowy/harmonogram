from dataclasses import dataclass

from harmonogram.rules.StudentRules import StudentRules
from ..containers.Timetable import Timetable


@dataclass
class Group(object):
    field_of_study: str
    name: str
    students_count: int
    timetable: Timetable
    group_points: int

    def __init__(self, field_of_study, name, students_count, timetable):
        self.field_of_study = field_of_study
        self.name = name
        self.students_count = students_count
        self.timetable = timetable
        self.timetable.rules = StudentRules()
        self.group_points = self.count_points()
        print("Group points: " + str(self.group_points))

    def count_points(self):
        self.timetable.rules = StudentRules()
        self.timetable.count_all()
        return self.timetable.total_points

    def get_timetable(self):
        return self.timetable

    def add_course_to_timetable(self, course):
        return self.timetable.add_course(course)
