import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from harmonogram.containers.Timetable import Timetable
from harmonogram.dto.Courses import Courses
from harmonogram.dto.Course import Course
from harmonogram.dto.Group import Group
from harmonogram.dto.Lecturer import Lecturer
from harmonogram.selenium_chromedriver.parser.AGHTimetableParser import TimetableParser
from harmonogram import Initializer

class WholeTimetable:
    def __init__(self, timetable='http://planzajec.eaiib.agh.edu.pl/view/timetable/490?date=2019-03-25'):
        self.timetableURL = timetable
        self.stringGroups = ['(1[^a])', '(1[^b])', '(2[^a])', '(2[^b])', '(3[^a])', '(3[^b])', '(4[^a])', '(4[^b])', '(5[^a])', '(5[^b])']
        self.groups = list()
        self.whole_points = 0
        self.initGroups()
        self.bigTimeTable = Timetable([])
        self.checkHours()
        self.bigTimeTable.courses = self.courses.courses
        self.changeGroupNameToNormal()
        # print(self.courses.courses[5].students_group)
        # print(self.courses.courses[5].course_type)
        # print('buba')
        # print(self.groups[2].name)
        # print(len(self.courses.courses))


    def checkHours(self):
        for c in self.courses.courses:
            if c.start_time.time() > c.end_time.time():
                c.start_time, c.end_time = c.end_time, c.start_time
                print("zamieniam")

    def changeGroupNameToNormal(self):
        for i in range(len(self.groups)):
            self.groups[i].name = self.groups[i].name[1] + self.groups[i].name[4]

    def initGroups(self):
        parser = Initializer.Initializer()
        driver = parser.initialize_webdriver(url=self.timetableURL)
        self.courses = parser.parse_courses(web_driver=driver)
        # print(len(self.courses.courses))
        for strGroup in self.stringGroups:
            actualGroup = parser.count_points_for_group(parsed_courses=self.courses, group=strGroup)
            self.groups.append(actualGroup)
            self.whole_points += actualGroup.group_points
        driver.quit()

    def printCourse(self, course):
        print(course.students_group)
        print(course.name)
        print(course.course_type)
        print(course.start_time.time())
        print(course.end_time.time())
        if course.start_time.time() < course.end_time.time():
            print("jupi!")
        print(course.day_of_week)
        print("-------------------------------")

    def findGroupByName(self, groupName):
        for g in self.groups:
            if g.name == groupName:
                return g

        # print("Poszukuje grupy:" + groupName)
        # print("Rozważam grupy:")

        for g in self.groups:
            # print(g.name[0])
            if g.name[0] == groupName[1]:
                return g
        return None

    def changeIsPossible(self, course1, course2):
        start_time1 = course1.start_time.time()
        end_time1 = course1.end_time.time()
        start_time2 = course2.start_time.time()
        end_time2 = course2.end_time.time()
        day1 = course1.day_of_week
        day2 = course2.day_of_week
        group1_name = course1.students_group
        group2_name = course2.students_group
        group1 = self.findGroupByName(group1_name)
        group2 = self.findGroupByName(group2_name)
        if (group1 or group2) is None:
            print("Któraś grupa nie istnieje")
            print(group1_name)
            print(group2_name)
        for c in group1.timetable.courses:
            if c.day_of_week != day2:
                continue
            if (c.start_time.time() > start_time2 and c.start_time.time() < end_time2) \
                or (c.end_time.time() > start_time2 and c.end_time.time() < end_time2):
                return False
        for c in group2.timetable.courses:
            if c.day_of_week != day1:
                continue
            if (c.start_time.time() > start_time1 and c.start_time.time() < end_time1) \
                or (c.end_time.time() > start_time1 and c.end_time.time() < end_time1):
                return False
        return True



    def findPotentialCourses(self, course):
        potentianCourses = list()
        for c in self.courses.courses:
            if c.name == course.name \
                    and c.students_group != course.students_group \
                    and c.course_type == course.course_type \
                    and c.lecturer == course.lecturer \
                    and self.changeIsPossible(c, course):
                potentianCourses.append(c)
        PC = Courses(potentianCourses)
        return PC

    def calculatePointsAfterChange(self, course1, course2):
        new_score = self.whole_points
        group1_name = course1.students_group
        group2_name = course2.students_group
        group1 = self.findGroupByName(group1_name)
        group2 = self.findGroupByName(group2_name)

        new_score -= group1.group_points
        new_score -= group2.group_points
        for c1 in group1.timetable.courses:
            if c1.name == course2.name and c1.course_type == course2.course_type:
                c1.start_time = course2.start_time
                c1.end_time = course2.end_time
                new_score += group1.count_points()
                c1.start_time = course1.start_time
                c1.end_time = course1.end_time
                break

        for c2 in group2.timetable.courses:
            if c2.name == course1.name and c2.course_type == course1.course_type:
                c2.start_time = course1.start_time
                c2.end_time = course1.end_time
                new_score += group2.count_points()
                c2.start_time = course2.start_time
                c2.end_time = course2.end_time
                break

        return new_score

    def swapCourses(self, course1, course2):
        group1_name = course1.students_group
        group2_name = course2.students_group
        group1 = self.findGroupByName(group1_name)
        group2 = self.findGroupByName(group2_name)

        self.whole_points -= group1.group_points
        self.whole_points -= group2.group_points
        for c1 in group1.timetable.courses:
            if c1.name == course2.name and c1.course_type == course2.course_type:
                c1.start_time = course2.start_time
                c1.end_time = course2.end_time
                self.whole_points += group1.count_points()
                break

        for c2 in group2.timetable.courses:
            if c2.name == course1.name and c2.course_type == course1.course_type:
                c2.start_time = course1.start_time
                c2.end_time = course1.end_time
                self.whole_points += group2.count_points()
                break

    def optimize(self):
        PTI = list()

        numberOfChanges = 0
        # print(len(self.courses.courses))
        # i = 0
        for course in self.courses.courses:
            # print(i)
            # i += 1
            # print(course.students_group)
            if course.students_group:
                PTI.append(course)
        possibleToImprove = Courses(PTI)
        # print(len(possibleToImprove.courses))
        # i = 0
        for course in possibleToImprove.courses:
            # print("Wypisuje kurs: " + str(i))
            # i += 1
            # self.printCourse(course)
            optionalCourses = self.findPotentialCourses(course)
            # print("Znalazłem potencjalne kursy do zamiany")
            if len(optionalCourses.courses) == 0:
                continue
            actualBestChoice = optionalCourses.courses[0]
            actualBestScore = self.whole_points
            # print("start przeszukiwania czy opłaca się z czymś zamienić")
            for maybe in optionalCourses.courses:
                points_afterChange = self.calculatePointsAfterChange(course, maybe)
                if points_afterChange > actualBestScore:
                    actualBestChoice = maybe
                    actualBestScore = points_afterChange
            # print("Czy zamieniamy")
            if actualBestScore > self.whole_points:
                self.swapCourses(actualBestChoice, course)
                numberOfChanges += 1
                # print("zamieniliśmy!")
        print("Zamian było: ")
        print(numberOfChanges)
        print("teraz za plan jest punktów: ")
        print(self.whole_points)

if __name__ == '__main__':
    w = WholeTimetable()
    print("punkty na start:")
    print(w.whole_points)
    for c in w.courses.courses:
        w.printCourse(c)
    print("...")
    w.optimize()
