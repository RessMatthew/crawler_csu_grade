from bs4 import BeautifulSoup

from Response.EducationalAdministration import getEducationalAdministrationResponseWithEdge, \
    getEducationalAdministrationResponseWithChrome
from Response.InformationPortal import getInformationPortalResponseWithEdge, getInformationPortalResponseWithChrome
from Response.MyGrades import getMyGradeResponseWithEdge, getMyGradeResponseWithChrome
from Tools.HTMLParse import printResult, getCourseTotal_int, addCourse

# Edge版
# response = getInformationPortalResponseWithEdge()
# response = getEducationalAdministrationResponseWithEdge()
response = getMyGradeResponseWithEdge()

# Chrome
# response = getInformationPortalResponseWithChrome()
# response = getEducationalAdministrationResponseWithChrome()
# response = getMyGradeResponseWithChrome()

##########################
# print(response.text) # 测试是否登入成功
##########################

bsObj = BeautifulSoup(response.text, "html.parser")  # 将请求的我的成绩响应文本解析为bs4对象

courseTotal_int = getCourseTotal_int(bsObj)  # 当前已有成绩科目数量

printResult(courseTotal_int, bsObj)  # 输出所有科目结果

##########################
# addCourse(courseTotal_int, bsObj)  # 持久化各科成绩
##########################
