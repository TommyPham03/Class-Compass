import Course


class Major:
    def __init__(self, freshmen_fall, freshmen_spring, sophomore_fall, sophomore_spring, junior_fall, junior_spring, senior_fall, senior_spring):
        self.Freshmen_Fall = freshmen_fall
        self.Freshmen_Spring = freshmen_spring
        self.Sophomore_Fall = sophomore_fall
        self.Sophomore_Spring = sophomore_spring
        self.Junior_Fall = junior_fall
        self.Junior_Spring = junior_spring
        self.Senior_Fall = senior_fall
        self.Senior_Spring = senior_spring

dr_lst = ["course_database/CS.txt","course_database/MATH.txt","course_database/blank.txt"]

subjects = Course.create(dr_lst)

CSlist = subjects[0]
MATHlist = subjects[1]
Nonelist = subjects[2]

MATHlist.search("1914")

ComputerScience = Major(
                        [MATHlist.search("1914"), Nonelist.search("1001"), CSlist.search("1324"), Nonelist.search("1001"), Nonelist.search("1001")],
                        [MATHlist.search("2924"), CSlist.search("2334"), Nonelist.search("1001"), Nonelist.search("1001")],
                        [MATHlist.search("2934"), Nonelist.search("1001"), CSlist.search("2813"), CSlist.search("2413"), Nonelist.search("1001")],
                        [Nonelist.search("1001"), CSlist.search("2614"), Nonelist.search("1001"), CSlist.search("3323")],
                        [CSlist.search("3203"), CSlist.search("3113"), CSlist.search("3823"), MATHlist.search("3003"), Nonelist.search("1001")],
                        [MATHlist.search("3333"), CSlist.search("4003"), MATHlist.search("4753"), Nonelist.search("1001"), Nonelist.search("1001")],
                        [CSlist.search("4003"), CSlist.search("4413"), CSlist.search("4173"), CSlist.search("4513"), CSlist.search("4003")],
                        [CSlist.search("4273"), CSlist.search("4473"), CSlist.search("4003"), Nonelist.search("1001"), Nonelist.search("1001")])



ComputerScienceSemesters = [ComputerScience.Freshmen_Fall, ComputerScience.Freshmen_Spring, ComputerScience.Sophomore_Fall, ComputerScience.Sophomore_Spring, ComputerScience.Junior_Fall, ComputerScience.Junior_Spring, ComputerScience.Senior_Fall, ComputerScience.Senior_Spring]

