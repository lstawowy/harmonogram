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

    def count_all(self):
        self.total_points = 0
        for i in range(len(self.courses) - 1): #Czemu -2? to jakis bug moim zdaniem... powinno być -1 i tak zostawiam
            self.count_break_time_points(i)

    def count_break_time_points(self, i):
        if self.courses[i].day_of_week == self.courses[i + 1].day_of_week:
            time = (self.courses[i].end_time.timestamp() - self.courses[i + 1].start_time.timestamp())
            if time == 0 and self.courses[i].room != self.courses[i + 1].room: #Zmieniłam na != bo punkty za teleport są ujemnejakby coś nie działało :D Czemu jeśli jest jeden kurs zaraz po drugim i są w tej samej sali to są punkty ujemne za teleportacje, a jakby były w różnych salach to by nie było punktów za teleportację?
                self.total_points += self.rules.points_for_teleport
            if time < 15 <= 0:
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
        self.count_all()

    def remove_course(self, course):
        self.courses.remove(course)
        self.count_all()
