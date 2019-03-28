import re
import time

from selenium import webdriver


def initialize_webdriver():
    driver = webdriver.Chrome('driver/chromedriver')
    driver.get('http://planzajec.eaiib.agh.edu.pl/view/timetable/490?date=2019-03-25')
    courses = driver.find_elements_by_class_name('fc-content')
    for course in courses:
        parse_text(course.text)
    time.sleep(5)  # Let the user actually see something!
    driver.quit()


def parse_text(course):
    lines = course.split('\n')
    print("Time: " + lines[0])
    if 'grupa' in lines[1]:
        splitted = lines[1].split('grupa')
        print("Course: " + splitted[0])
        if len(splitted) > 1:
            print("Group: " + splitted[1])
    else:
        print("Course: " + lines[1])
    splitted = course.split('prowadzący:')
    if len(splitted) >= 1:
        room = find_from_regex('Sala: ([A-Z]-[1-9] [^\s-]*)', splitted[0])
        if room:
            print('Room:' + room.group(1))
    if len(splitted) > 1:
        print("Lecturer: " + splitted[1])


def find_from_regex(regex, text):
    m = re.search(regex, text)
    if m:
        return m


if __name__ == '__main__':
    initialize_webdriver()
