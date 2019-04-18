import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from harmonogram.containers.Timetable import Timetable
from harmonogram.dto.Courses import Courses
from harmonogram.dto.Group import Group
from harmonogram.dto.Lecturer import Lecturer
from harmonogram.selenium_chromedriver.parser.AGHTimetableParser import TimetableParser

DEFAULT_LECTURER = 'Kutt'
DEFAULT_GROUP_REGEX = '(5[^a])'
TIMETABLE_URL = 'http://planzajec.eaiib.agh.edu.pl/view/timetable/490?date=2019-03-25'
EXECUTABLE_PATH = 'selenium_chromedriver/driver/chromedriver'


class Initializer(object):

    @staticmethod
    def count_points_for_group(parsed_courses, group=DEFAULT_GROUP_REGEX):
        timetable = Timetable([])
        timetable.courses = parsed_courses.find_by_group(group_regex=group)
        group = Group(name=group, field_of_study=None, timetable=timetable, students_count=30)
        return group

    @staticmethod
    def count_points_for_lecturer(parsed_courses, lecturer_name=DEFAULT_LECTURER):
        timetable = Timetable([])
        timetable.courses = parsed_courses.find_by_lecturer(lecturer=lecturer_name)
        lecturer = Lecturer(name=lecturer_name, timetable=timetable)
        return lecturer

    @staticmethod
    def parse_courses(web_driver):
        raw_courses = web_driver.find_elements_by_class_name('fc-content')
        parsed_courses = Courses()

        time.sleep(2)
        for i in range(len(raw_courses)):
            timetable_parser = TimetableParser()
            # timetable_parser.parse_text(raw_courses[i].text)
            parsed_courses.add_course(course=timetable_parser.parse_course(raw_courses[i]))
        return parsed_courses

    @staticmethod
    def initialize_webdriver(url):
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        chrome_driver = webdriver.WebDriver(executable_path=EXECUTABLE_PATH, chrome_options=options)
        chrome_driver.get(url)
        chrome_driver.set_window_size(1200, 1080)
        return chrome_driver


if __name__ == '__main__':
    parser = Initializer()
    driver = parser.initialize_webdriver(url=TIMETABLE_URL)
    time.sleep(2)
    courses = parser.parse_courses(web_driver=driver)

    parser.count_points_for_lecturer(parsed_courses=courses)
    # parser.count_points_for_group(parsed_courses=courses)

    time.sleep(2)
    driver.quit()
