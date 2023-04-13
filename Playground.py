from Course import Course
from Planner import PlanSemester

java_I0 = Course("Introduction to Computer Programming for Non-Programmers", "CS1324", False)

java_I1 = Course("Introduction to Computer Programming for Programmers", "CS1323", False)

java_I2 = Course("Java for Programmers", "CS1321", False)

calc_I0 = Course("Calculus & Analyt Geometry I", "MATH1823", False)

fman_engr = Course("Freshman Engineering Experience", "ENGR1411", False)

course_list = []
course_list.extend([java_I0, java_I1, java_I2, calc_I0, fman_engr])

Plan1 = PlanSemester(12, 2, course_list)
print("Here are the courses you can take: \n" )
Plan1.mk_course()


