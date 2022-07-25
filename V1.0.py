from bs4 import BeautifulSoup
from Response.MyGrades import getMyGradeResponse
from Tools.HTMLParse import getGradeById, printResult, getCourseTotal_int

response = getMyGradeResponse()

# print(response.text) # 测试是否登入成功

bsObj = BeautifulSoup(response.text, "html.parser")  # 将请求的我的成绩响应文本解析为bs4对象

courseTotal_int = getCourseTotal_int(bsObj)  # 当前已有成绩科目数量

printResult(courseTotal_int, bsObj)  # 输出所有科目结果
