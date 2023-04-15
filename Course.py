# make a class that defines a course and its contents
class Course:
    # method one: constructor
    def __init__(self, name, code, lst_pr, taken):
        self.name = name
        self.code = code
        self.lst_pr = lst_pr
        # put this somewhere else later on actually
        # insert something here that converts all the titles from lst_pr to their matching course objects, assuming they have been made
        self.taken = taken

    # method two: retrieve name
    def getName(self):
        return self.name

    # method three: retrieve class code
    def getCode(self):
        return self.code

    # method four: retrieve whether class has been taken or not
    def is_taken(self):
        return self.taken

    # method five: retrieve hours the class is worth using course code
    def getHours(self):
        code = self.getCode()
        hour = int(code[-1])
        return hour

    # method eight: get subject
    def getSubject(self):
        return self.code[:-4]

    # method seven: print
    def print(self):
        print("Course Name: " + self.getName() + "\n"
              + "Subject: " + self.getSubject() + "\n"
              + "Course Code: " + self.getCode() + "\n"
              + "Course Hours: " + str(self.getHours()) + " Hour(s)" + "\n"
              + "Taken: " + str(self.is_taken()) + "\n")
    # TODO: create a method that represents a user attempting to take a course
    def take(self): # use for a button for HTML
        return all(any(sub_lst[i].is_taken() for sub_lst in self.lst_pr) for i in range(len(self.lst_pr[0])))
    def select(self): # use for a button in HTML
        if self.take():
            print("You may take " + self.getName())
    # When a user selects a class to mean that they have taken it, this method will be invoked
    def report_taken(self):
        self.taken = True


class Reader: # TODO: Create a library cataloging of groups of courses based on their course Strings
    str = "Programming Structures and Abstractions,CS2334,CS1321/CS1323/CS1324 MATH1523+,False"
    listy = str.split(",")
    print(listy)
    prereq = listy[2].split(" ")
    for i, coursey in enumerate(prereq):
        prereq[i] = coursey.split("/")
    print(prereq)
    course = Course(listy[0], listy[1], prereq, listy[3])
    course.print()
    # course.take() this method has an error.
    # TODO: Create a method that takes the strings of prerequisite courses and finds its course object equivalent
