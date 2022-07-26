import pymongo


# 连接mongoDB
client = pymongo.MongoClient(host='180.76.233.143', port=27017)
# 指定数据库
db = client['grades']
# 指定集合
collection = db['course']

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_one(student)

print(result)