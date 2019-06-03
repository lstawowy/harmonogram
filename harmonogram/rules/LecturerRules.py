from .Rules import Rules


class LecturerRules(Rules):
    def __init__(self):
        super().__init__()
        self.points_for_teleport = -10

        self.max_courses_per_day = 6

        self.points_up_to_15min_break = 10
        self.points_15min_to_1h_break = 7
        self.points_1h_to_2h_break = 2
        self.points_2h_to_4h_break = -1
        self.points_4h_and_above_break = -5

        self.points_lecture_before_course = 3
        self.points_students_thursday = 0
        self.points_free_friday = 7
