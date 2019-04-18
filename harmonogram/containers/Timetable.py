from dataclasses import dataclass

from ..rules.Rules import Rules


@dataclass
class Timetable(object):
    courses: list
    rules: Rules
    total_points: int

    def __init__(self, courses):
        self.courses = courses
        self.total_points = 0
        self.count_all()

    def parse_data(self):
        courses = None
        for course in self.courses:
            courses += course.show()

    def count_all(self):
        for i in range(len(self.courses) - 2):
            self.count_break_time_points(i)

    def count_break_time_points(self, i):
        # if self.courses[i].day_of_week == self.courses[i + 1].day_of_week:
        if True:
            time = (self.courses[i].end_time.timestamp() - self.courses[i + 1].start_time.timestamp())
            if time == 0 and self.courses[i].room == self.courses[i + 1].room:
                self.total_points += self.rules.points_for_teleport
            if time < 15:
                self.total_points += self.rules.points_up_to_15min_break
            if 15 < time < 60:
                self.total_points += self.rules.points_15min_to_1h_break
            if 60 < time < 120:
                self.total_points += self.rules.points_15min_to_1h_break
            if 120 < time < 180:
                self.total_points += self.rules.points_15min_to_1h_break
            if time > 180:
                self.total_points += self.rules.points_15min_to_1h_break

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)
