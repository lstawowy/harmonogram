from dataclasses import dataclass


@dataclass
class Timetable(object):
    courses: list

    def __init__(self, courses):
        self.courses = courses

    def parse_data(self):
        pass

    def count(self):
        pass
