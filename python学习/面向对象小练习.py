from datetime import datetime
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Student(Person):
    count=0
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        Student.count+=1
        self.stu_id=f"{datetime.now().year}{self.count:03d}"
        self.score={}

    def add_score(self,subject,score):
        self.score[subject]=score

    def avg_score(self):
        if self.score:
            return sum(self.score.values())/len(self.score)
        else:
            return 0

    def __str__(self):
        return f"我叫{self.name},年龄为{self.age},性别为{self.gender},平均分为{self.avg_score()}，成绩为{self.score}"

class Manager :
    def __init__(self):
        self.stu_list=[]

    #添加学生
    def add_student(self):
        name=input("请输入姓名")
        age = input("请输入年龄")
        gender = input("请输入性别")
        stu=Student(name,age,gender)
        self.stu_list.append(stu)
        print(f"恭喜添加学生成功，该学生学号为：{stu.stu_id}")


    def  del_student(self):
        sid=input("请输入学号：")
        for stu in self.stu_list:
            if stu.stu_id==sid:
                self.stu_list.remove(stu)
                print("删除成功")
            else:
                print("学号有问题")

    def show_student(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print("列表里暂无学生")

    def set_score(self):
        sid=input("请输入学号：")
        for stu in self.stu_list:
            if stu.stu_id==sid:
                score_str=input("请输入：学科-成绩 学科-成绩")
                list1=score_str.split(" ")
                for item in list1:

                    subject,score= item.split("-")
                    stu.add_score(subject,int(score))
                print("添加成功")
                return
        print("学号有问题")

    def run(self):
        while True:
            print('************学生管理************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')

            chocie = input('请输入操作编号：')
            if chocie == '1':
                self.add_student()
            elif chocie == '2':
                self.del_student()
            elif chocie == '3':
                self.show_student()
            elif chocie == '4':
                self.set_score()
            elif chocie == '5':
                print('再见！')
                break
            else:
                print('输入有误！')

m1 = Manager()
m1.run()