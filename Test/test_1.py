from Domain.Course import Course
from Tools.MongoDB import MongoDB

# 测试MongoDB插入操作
mongodb = MongoDB()
mongodb.connect()
course = Course("测试", "100")
mongodb.insert_course(course)
