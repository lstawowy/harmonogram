from dataclasses import dataclass


@dataclass
class Lecturers(object):
    lecturers: list
    total_points: int

    def __init__(self, lecturers):
        self.lecturers = lecturers
        self.count_points()

    def count_points(self):
        for lecturer in self.lecturers:
            self.total_points += lecturer.count_points()
