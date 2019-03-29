import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from harmonogram.selenium.parser.AGHTimetableParser import TimetableParser

EXECUTABLE_PATH = 'driver/chromedriver'


class TimetableParserSelenium(object):

    def initialize_webdriver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH, chrome_options=options)
        driver.get('http://planzajec.eaiib.agh.edu.pl/view/timetable/490?date=2019-03-25')
        courses = driver.find_elements_by_class_name('fc-content')
        time.sleep(2)
        for course in courses:
            parser = TimetableParser()
            parser.parse_text(course.text)
        time.sleep(2)  # Let the user actually see something!
        driver.quit()


if __name__ == '__main__':
    parser = TimetableParserSelenium()
    parser.initialize_webdriver()
