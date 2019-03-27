from dataclasses import dataclass


@dataclass
class Group:
    field_of_study: str
    name: str
    students: list
    harmonogram: Harmonogram
    total_points: int

    def __init__(self, field_of_study, name, students, harmonogram, total_points):
        self.field_of_study = field_of_study
        self.name = name
        self.students = students
        self.harmonogram = harmonogram
        self.total_points = total_points

    def get_harmonogram(self):
        return self.harmonogram

    def add_course_to_harmonogram(self, course):
        return self.harmonogram.add_course(course)

    def count_total(self):
        self.total_points = 1
