import re


class TimetableParser(object):
    def __init__(self):
        pass

    INZ_TITLE = 'inż. '
    MGR_TITLE = 'mgr '
    HAB_TITLE = 'hab. '
    DR_TITLE = 'dr '
    PROF_TITLE = 'prof. '

    WYK_TYPE = 'Wyklad'
    AUD_TYPE = 'aud. '
    PROJ_TYPE = 'proj. '
    LAB_TYPE = 'lab. '
    CW_TYPE = 'Ćw. '

    def parse_text(self, course):
        lines = course.split('\n')
        print("Time: " + lines[0])
        course_type = self.parse_course_type(re.search(',(.+)', lines[1]).group(1))
        print("Course type: " + course_type)
        if 'grupa' in lines[1]:
            splitted = lines[1].split('grupa')

            print("Course: " + re.search('(.+?(?=,))', splitted[0]).group(1))
            if len(splitted) > 1:
                print("Group: " + splitted[1])
        else:
            print("Course: " + re.search('(.+?(?=,))', lines[1]).group(1))
        splitted = course.split('prowadzący:')
        if len(splitted) >= 1:
            room = self.find_from_regex('Sala: ([A-Z]-[1-9] [^\s-]*)', splitted[0])
            if room:
                print('Room: ' + room.group(1))
        if len(splitted) > 1:
            titles = self.parse_titles(splitted[1])
            name = self.find_from_regex('.+?(?=,)', splitted[1])
            if name:
                print("Lecturer: " + titles + name.group(0))

    def parse_titles(self, splitted):
        titles = ''
        is_prof = self.find_from_regex('prof', splitted)
        if is_prof:
            titles += self.PROF_TITLE
        is_dr = self.find_from_regex('dr', splitted)
        if is_dr:
            titles = titles + self.DR_TITLE
            is_hab = self.find_from_regex('hab', splitted)
            if is_hab:
                titles += self.HAB_TITLE
        is_mgr = self.find_from_regex('mgr', splitted)
        if is_mgr:
            titles += self.MGR_TITLE
        is_inz = self.find_from_regex('(inz)|(inż)', splitted)
        if is_inz:
            titles += self.INZ_TITLE
        return titles

    def parse_course_type(self, splitted):
        type = ''
        is_cw = self.find_from_regex('([ĆćCc][Ww])', splitted)
        if is_cw:
            type += self.CW_TYPE
            type = self.determine_cw_type(splitted, type)
        else:
            is_wyk = self.find_from_regex('([Ww][Yy][Kk])', splitted)
            if is_wyk:
                type += self.WYK_TYPE
        return type

    def determine_cw_type(self, splitted, type):
        is_lab = self.find_from_regex('([Ll][Aa][Bb])', splitted)
        if is_lab:
            type += self.LAB_TYPE
        is_proj = self.find_from_regex('([Pp][Rr][Oo][Jj])', splitted)
        if is_proj:
            type += self.PROJ_TYPE
        is_aud = self.find_from_regex('([Aa][Uu][Dd])', splitted)
        if is_aud:
            type += self.AUD_TYPE
        return type

    @staticmethod
    def find_from_regex(regex, text):
        m = re.search(regex, text)
        if m:
            return m
