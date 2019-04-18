from dataclasses import dataclass


@dataclass
class Courses(object):
    courses: list

    def __init__(self, courses=[]):
        self.courses = courses

    def find_by_lecturer(self, lecturer):
        result = []
        for course in self.courses:
            if course.match_lecturer(lecturer=lecturer):
                result.append(course)
        return result

    def find_by_group(self, group):
        result = []
        for course in self.courses:
            if course.match_students_group(group=group):
                result.append(course)
        return result

    def find_by_course_name_and_type(self, name, course_type):
        result = []
        for course in self.courses:
            if course.match_course(name, course_type):
                result.append(course)
        return result

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)
