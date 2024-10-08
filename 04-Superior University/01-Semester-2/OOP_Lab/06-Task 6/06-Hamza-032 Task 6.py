class Course:
    def __init__(self,course_code,course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        return f"Course Code : {self.course_code}  \nCourse Name : {self.course_name}"

class UndergraduateCourse(Course):
    def __init__(self, course_code, course_name,year_level):
        super().__init__(course_code, course_name)
        self.year_level = year_level

    def additional_info(self):
        return f"Year Level : {self.year_level}"


class GraduateCourse(Course):
    def __init__(self, course_code, course_name,research_area):
        super().__init__(course_code, course_name)
        self.research_area = research_area

    def additional_info(self):
        return f"Research Area : {self.research_area}"


def register_course():
    course_type = input("Enter Course Type : (Graduate/Undergraduate)")
    course_code = input("Enter Course Code : ")
    course_name = input("Enter Course Name : ")

    if course_type=="Undergraduate":
        year_level=input("Enter Your Year Level : ")
        course = UndergraduateCourse(course_code,course_name,year_level)
    elif course_type=="Graduate":
        research_area=input("Enter Your Research Area : ")
        course = GraduateCourse(course_code,course_name,research_area)
    else:
        print("Invalid course type! Plz enter valid course type")
        return

    print(course.display_info())
    print(course.additional_info())  

register_course()              