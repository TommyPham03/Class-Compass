from Course import Course
class PlanSemester:
    def __init__(self, hours, semesters,course_list):
        self.hours = hours
        self.semesters = semesters
        self.course_list = course_list
    def get_hours(self):
        return self.hours
    def courses(self):
        print("Success! ") + self.course.print()

    def mk_course(self):
        limit = self.get_hours()
        idx = 0
        list_i = 0
        while idx < limit:
            course = self.course_list[list_i]
            course.print()
            idx += course.getHours()





