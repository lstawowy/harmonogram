import re
from datetime import datetime

from dataclasses import dataclass


@dataclass
class Course(object):
    name: str
    day_of_week: int
    start_time: datetime
    end_time: datetime
    lecturer: str
    students_group: str
    room: str
    course_type: str

    def __init__(self, name, day_of_week, start_time, end_time, lecturer, room, course_type, students_group):
        self.name = name
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.lecturer = lecturer
        self.room = room
        self.course_type = course_type
        self.students_group = students_group

    def match_lecturer(self, lecturer_regex):
        if self.lecturer:
            if self.find_from_regex(lecturer_regex, self.lecturer):
                return self

    def match_students_group(self, group_regex):
        if self.students_group:
            if self.find_from_regex(group_regex, self.students_group):
                return self
        else: #po co ta funkcja skoro zawsze zwraca self? xD nie zawsze
            return self

    def match_room(self, room):
        if self.room.find(room):
            return self

    def match_course(self, name, course_type):
        if self.name.find(name) and self.course_type.find(course_type):
            return self

    def show(self):
        return self.name + self.lecturer + str(self.start_time) + self.students_group

    @staticmethod
    def find_from_regex(regex, text):
        m = re.search(regex, text)
        if m:
            return m
