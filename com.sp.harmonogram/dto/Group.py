from dataclasses import dataclass


@dataclass
class Group(object):
    field_of_study: str
    name: str
    students: list
    timetable: Timetable
    total_points: int

    def __init__(self, field_of_study, name, students, timetable, total_points):
        self.field_of_study = field_of_study
        self.name = name
        self.students = students
        self.timetable = timetable
        self.total_points = total_points

    def get_timetable(self):
        return self.timetable

    def add_course_to_timetable(self, course):
        return self.timetable.add_course(course)

    def count_total(self):
        self.total_points = 1
