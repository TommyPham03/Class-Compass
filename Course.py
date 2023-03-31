# make a class that defines a course and its contents
class Course:
    # method one: constructor
    def __init__(self, name, code, taken):
        self.name = name
        self.code = code
        self.taken = taken
    # method two: retrieve name
    def getName(self):
        print(self.name)
    # method three: retrieve class code
    def getCode(self):
        print(self.code)
    #method four: retrieve whether class has been taken or not
    def isTaken(self):
        print(self.taken)
Java_I = Course("Introduction to Java", "CS1321", True)
Java_I.getName()
Java_I.getCode()
Java_I.isTaken()
