# make a class that defines a course and its contents
global subjects


class Course:
    # method one: constructor
    def __init__(self, name, code, lst_pr, taken):
        self.name = name
        self.code = code
        self.lst_pr = lst_pr
        self.taken = taken

    # method two: retrieve name
    def get_name(self):
        return self.name

    # method three: retrieve class code
    def get_code(self):
        return self.code

    def get_int(self):
        return self.code[-4:] # returns the last 4 chars

    # method four: retrieve whether class has been taken or not
    def is_taken(self):
        return self.taken

    # method five: retrieve hours the class is worth using course code
    def get_hours(self):
        code = self.get_code()
        hour = int(code[-1])
        return hour

    # method eight: get subject
    def get_subject(self):
        return self.code[:-4] # returns all but the last 4 chars

    def get_pr_format(self):
        lst = []
        for idx, val in enumerate(self.lst_pr):
            for subidx, subval in enumerate(val):
                if subval == "None":
                    return subval
                lst.append(subval)
                if subidx < len(val) - 1:
                    lst.append("OR")
            if idx < len(self.lst_pr) - 1:
                lst.append("AND")
        return lst

    # method seven: print
    def print(self):
        print("Course Name: " + self.get_name() + "\n"
              + "Subject: " + self.get_subject() + "\n"
              + "Course Code: " + self.get_code() + "\n"
              + "Course Hours: " + str(self.get_hours()) + " Hour(s)" + "\n"
              + "Taken: " + str(self.is_taken()) + "\n"
              + "Prerequisites: " + str(self.get_pr_format()) + "\n")

    # TODO: create a method that represents a user attempting to take a course
    def take(self, SJTS):  # use for a button for HTML
        # lst_prq = []
        boo = False
        true_ct = 0
        for idx, ANDS in enumerate(self.lst_pr):
            or_val = False
            for sub_idx, OR in enumerate(ANDS):
                if OR == "None":
                    boo = True
                    pass
                else:
                    if or_val:
                        break
                    '''watch it'''
                    course = match_course(OR, SJTS)
                    # below if statement is crucial since we have many Subject objects
                    if course is None:
                        break
                    # print(course.get_name())
                    print(course.get_name() + ": " + str(course.is_taken()) + "\n")
                    if course.is_taken() == True:
                        true_ct = true_ct + 1
                        # print("counts: " + str(true_ct))
                        break
                if sub_idx == len(ANDS) and or_val == False:
                    print("TAKE " + str(self.get_name()) + ": FAIL" + "\n")
                    boo = False
            if true_ct >= len(self.lst_pr):
                boo = True

        # print(boo)
        return boo

    def select(self, SJTS):  # use for a button in HTML
        print("YOU ARE ATTEMPTING TO TAKE: " + self.get_name() + "\n")
        if self.take(SJTS):
            return print("You MAY take " + self.get_name() + "\n")
        return print("You CANNOT take " + self.get_name() + "\n")

    # When a user selects a class to mean that they have taken it, this method will be invoked
    def report_taken(self):
        self.taken = True
        print(self.name + " has been changed to TAKEN" + "\n")

    def report_not_taken(self):
        self.taken = False
        print(self.name + " has been changed to NOT TAKEN" + "\n")

    '''def pr_match(self, course):
        sujeto = nm[:-4]
        for idx in SJTS:
            idx.match_course(sujeto)'''


class Subject:
    def __init__(self, nm):
        self.nm = nm
        self.c_list = []

    def get_nm(self):
        return self.nm

    def add_course(self, course):
        self.c_list.append(course)

    def get_list(self):
        return self.c_list

    def search(self, nmbr):
        for crs in self.get_list():
            if str(crs.get_int()) == str(nmbr):
                return crs

        print("ERROR: " + str(nmbr) + " not yet existent in data provided")


class Reader:
    def __init__(self, txt):
        self.txt = txt

    def open(self):
        file = open(self.txt, 'r')
        courses = file.readlines()
        subject = Subject("nm")
        for i in courses:
            # print(i + "here")
            listy = i.split(",")
            prereq = listy[2].split(" ")

            for i, coursey in enumerate(prereq):
                prereq[i] = coursey.split("/")
            # print(prereq)
            course = Course(listy[0], listy[1], prereq, listy[3])
            subject.add_course(course)
        return subject

        # course.take() this method has an error.
        # TODO: Create a method that takes the strings of prerequisite courses and finds its course object equivalent



def match_course(course, sjts):
    for sjt in sjts:
        for crs in sjt.get_list():
            if crs.get_code() == course:
                return crs
        # raise ValueError("course '" + course + "' cannot be matched in the subject '" + self.get_nm() + "' :(.")

def extract_substring(s):
    start_index = s.index("/") + 1
    end_index = s.index(".")
    return s[start_index:end_index]
def create(src_lst):
    SJTS = []
    for dr in src_lst:
        SJT = Subject(extract_substring(dr))
        read = Reader(dr)
        subject = read.open()
        for crs in subject.get_list():
            SJT.add_course(crs)
        SJTS.append(SJT)
    return SJTS
def trial ():
    CSey = match_course("CS1321", subjects)
    CSey.report_taken()
    CSey.print()
    CSey.select(subjects)

    mathey = match_course("MATH1523", subjects)
    mathey.report_taken()
    mathey.print()
    mathey.select(subjects)

    CS_dos = match_course("CS2334", subjects)
    CS_dos.print()
    CS_dos.select(subjects)

    CS_tres = match_course("CS2413", subjects)
    CS_tres.print()
    CS_tres.select(subjects)

    CS_dos.report_taken()
    CS_tres.select(subjects)

    MATH_dos = match_course("MATH1914", subjects)
    MATH_dos.report_taken()
    CS_tres.select(subjects)


'''Add TXT file directories here'''
dr_lst = ["course_database/CS.txt","course_database/MATH.txt"]

subjects = create(dr_lst)
'''
MATH_dos = match_course("MATH1914", subjects)
print("INT: " + MATH_dos.get_int())
MATH_dos_copy = subjects[1].search("1914")
MATH_dos_copy.print()
print("INT: " + MATH_dos_copy.get_int())
'''



