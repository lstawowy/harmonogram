from .Rules import Rules


class LecturerRules(Rules):
    max_courses_per_day = 6

    points_up_to_15min_break = 10
    points_15min_to_1h_break = 7
    points_1h_to_2h_break = 2
    points_2h_to_4h_break = -1
    points_4h_and_above_break = -5
