from dataclasses import dataclass


@dataclass
class Lecturer:
    name: str
    timetable: Timetable
