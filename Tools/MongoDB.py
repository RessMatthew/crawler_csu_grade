import pymongo


class MongoDB:
    # course集合
    _collection = ''

    # Des       :   连接到180.76.233.143上grade数据库course集合
    # Parm      :   NULL
    # Return    :   NULL
    def connect(self):
        # 连接mongoDB
        client = pymongo.MongoClient(host='180.76.233.143', port=27017)
        # 指定数据库
        db = client['grades']
        # 指定集合
        self._collection = db['course']

    # Des       :   插入course集合到course集合
    # Parm      :   Course对象
    # Return    :   NULL
    def insert_course(self, course):
        course = {
            'course': course._name,
            'grade': course._grade,
        }
        self._collection.insert_one(course)
