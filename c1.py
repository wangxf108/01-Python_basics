
#类，对象
#实例化
#类的最基本的作用：封装



# 类就是一个模版，可以产生很多对象，不同的对象

# 类和对象
class Student():
    #可以定义若干变量
    sum = 0
    name = 'wang'
    age = 0

    # 构造函数
    def __init__(self, name, age):
        # 初始化对象的属性
        # 构造函数，不能添加return，只能返回None
        self.name = name         #左边的name是class中的定义的一个变量，右边的name是构造函数中的name，将右边的值传给左边
        self.age = age


    # 行为 与 特征
    def do_homework(self):
        print('homework')

student1 = Student('Jarry', 18)
student2 = Student('Mack', '33')
print(student1.name)
print(student2.name)
print(Student.name)
# student1.__init__()








# class Printer():
#     def print_file(self):
#         print('name:' + self.name)   #调用类的变量时，要加self
#         print('age:' + str(self.age))

# class StudentHomework():
#     homework_name = ''

#对类进行实例化
# student = Student()
# #实例化以后，调用类的方法
# student.print_file()

# 方法 和 函数的区别
# 方法：设计层面（面向对象）
# 函数：程序运行，过程的一种称谓

