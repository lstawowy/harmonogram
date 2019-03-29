from datetime import datetime

from dataclasses import dataclass


@dataclass
class Course(object):
    name: str
    day_of_week: int
    start_time: datetime
    end_time: datetime
    lecturer: str
    room: str
    is_lecture: bool

    def __init__(self, name, day_of_week, start_time, end_time, lecturer, room, is_lecture):
        self.name = name
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.lecturer = lecturer
        self.room = room
        self.is_lecture = is_lecture
