# make a class that defines a course and its contents
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
        return self.code[:-4]

    # method seven: print
    def print(self):
        print("Course Name: " + self.get_name() + "\n"
              + "Subject: " + self.get_subject() + "\n"
              + "Course Code: " + self.get_code() + "\n"
              + "Course Hours: " + str(self.get_hours()) + " Hour(s)" + "\n"
              + "Taken: " + str(self.is_taken()) + "\n")

    # TODO: create a method that represents a user attempting to take a course
    def take(self):  # use for a button for HTML
        return all(any(sub_lst[i].is_taken() for sub_lst in self.lst_pr) for i in range(len(self.lst_pr[0])))

    def select(self):  # use for a button in HTML
        if self.take():
            print("You may take " + self.getName())

    # When a user selects a class to mean that they have taken it, this method will be invoked
    def report_taken(self):
        self.taken = True


class Subject:
    def __init__(self, nm):
        self.nm = nm
        self.c_list = []

    def get_nm(self):
        return self.nm

    def add_course(self, course):
        self.c_list.append(course)

    def match_course(self, course):
        for i in self.c_list:
            if i.get_code() == course.get_code():
                return i
    def get_list(self):
        return self.c_list


class Reader:  # TODO: Create a library cataloging of groups of courses based on their course Strings
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


read = Reader('course_database/CS.txt')
subject = read.open()
for i in subject.get_list():
    i.print()
