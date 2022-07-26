from Domain.Course import Course


# Des       :   将html dataList 课程名和成绩爬出
# Parm      :   课程顺序ID
# Return    :   课程名与课程成绩str
def getGradeStrById(newCourseId, bsObj):
    courseId = "td_" + str(newCourseId)
    courseName = bsObj.find("td", {
        "id": courseId}).next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    courseGrade = bsObj.find("td", {
        "id": courseId}).next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    return courseName.get_text() + " : " + courseGrade.get_text()


# Des       :   将html dataList 课程名和成绩爬出
# Parm      :   课程顺序ID
# Return    :   Course对象
def getCourseById(newCourseId, bsObj):
    courseId = "td_" + str(newCourseId)
    courseName = bsObj.find("td", {
        "id": courseId}).next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
    courseGrade = bsObj.find("td", {
        "id": courseId}).next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
    return Course(courseName, courseGrade)


# Des       :   获取当前已有成绩科目数量
# Parm      :   bs4对象bsObj
# Return    :   课程总数
def getCourseTotal_int(bsObj):
    return len(bsObj.findAll("td", {"colspan": "21"}))


# Des       :   输出所有科目结果
# Parm      :   课程总数courseTotal_int，bs4对象bsObj
# Return    :   NULL
def printResult(courseTotal_int, bsObj):
    for i in range(1, courseTotal_int + 1):
        # print(getGradeStrById(i, bsObj))
        course = getCourseById(i, bsObj)
        course.printStr()


from Domain.Course import Course
from Tools.MongoDB import MongoDB


# Des       :   输出所有科目结果
# Parm      :   课程总数courseTotal_int，bs4对象bsObj
# Return    :   NULL
def addCourse(courseTotal_int, bsObj):
    mongodb = MongoDB()
    mongodb.connect()
    for i in range(1, courseTotal_int + 1):
        # print(getGradeStrById(i, bsObj))
        course = getCourseById(i, bsObj)
        mongodb.insert_course(course)
        # course.printStr()
