class Rules(object):
    def __init__(self):
        self.points_for_teleport = None

        self.max_courses_per_day = None

        self.points_up_to_15min_break = None
        self.points_15min_to_1h_break = None
        self.points_1h_to_2h_break = None
        self.points_2h_to_4h_break = None
        self.points_4h_and_above_break = None

        self.points_lecture_before_course = None
        self.points_students_thursday = None
        self.points_free_friday = None
