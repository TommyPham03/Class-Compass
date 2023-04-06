# make a class that defines a course and its contents
class Course:
    # method one: constructor
    def __init__(self, name, code, taken):
        self.name = name
        self.code = code
        self.taken = taken
    # method two: retrieve name
    def getName(self):
        return self.name
    # method three: retrieve class code
    def getCode(self):
        return self.code
    #method four: retrieve whether class has been taken or not
    def isTaken(self):
        return self.taken
    #method five: retrieve hours the class is worth using course code
    def getHours(self):
        code = self.getCode()
        hour = int(code[-1])
        return hour
    #method eight: get subject
    def getSubject(self):
        return self.code[:-4]
    #method seven: print
    def print(self):
        print("Course Name: " + self.getName() + "\n"
              + "Subject: " + self.getSubject() + "\n"
              + "Course Code: " + self.getCode() + "\n"
              + "Course Hours: " + str(self.getHours()) + " Hour(s)" + "\n"
              + "Taken: " + str(self.isTaken()) + "\n")

# Java_I = Course("Introduction to Java", "CS1321", True)
# Java_I.print()
#
# Calc_I_0 = Course("Calculus & Analyt Geometry I", "MATH1823", True)
# Calc_I_0.print()



