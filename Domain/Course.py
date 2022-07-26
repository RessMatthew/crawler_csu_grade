class Course:
    # 定义私有属性,私有属性在类外部无法直接进行访问
    _name = ''
    _grade = ''

    # 定义构造方法
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def printStr(self):
        print(str(self._name) + " : " + str(self._grade))
