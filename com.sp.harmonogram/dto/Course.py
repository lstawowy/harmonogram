from dataclasses import dataclass


@dataclass
class Course:
    name: str
    day_of_week: int
    time: time
    lecturer: Lecturers.MILLER
    room: Rooms.C315
