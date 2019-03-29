from dataclasses import dataclass

from ..rules.Rules import Rules


@dataclass
class Timetable(object):
    courses: list
    rules: Rules
    total_points: int

    def __init__(self, courses):
        self.courses = courses

    def parse_data(self):
        courses = None
        for course in self.courses:
            courses += course.show()

    def count_all(self):
        for i in range(len(self.courses) - 1):
            self.count_break_time_points(i)

    def count_break_time_points(self, i):
        if self.courses[i].day_of_week == self.courses[i + 1].day_of_week:
            time = (self.courses[i].end_time - self.courses[i].start_time)
            if time < 15:
                self.total_points += self.rules.points_up_to_15min_break
            if time > 15 & time < 60:
                self.total_points += self.rules.points_15min_to_1h_break
            if time > 60 & time < 120:
                self.total_points += self.rules.points_15min_to_1h_break
            if time > 120 & time < 180:
                self.total_points += self.rules.points_15min_to_1h_break
            if time > 180:
                self.total_points += self.rules.points_15min_to_1h_break

    def add_course(self, course):
        self.courses.append(course)
