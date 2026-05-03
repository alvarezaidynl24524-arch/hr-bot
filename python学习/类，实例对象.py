from datetime import datetime

class Person:
    def __init__(self,name,age,gender,id_card):
        self.name=name
        self._age=age
        self.__gender=gender
        self.__id_card=id_card
    def speak(self,msg):
        print(f"我叫{self.name},年龄{self.age},性别{self.gender},说{msg}")

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age=value

    @property
    def id_card(self):
        return self.__id_card[:6]+"########"+self.__id_card[-4:]
    @id_card.setter
    def id_card(self,value):
        print("不允许修改")


class Woker:
    def __init__(self,company):
        self.company=company
    def woker(self):
        print(f"我在{self.company}打工")

    # fruits="西瓜"
    #
    # @classmethod
    # def change(cls,value):
    #     cls.fruits=value
    #
    #
    # @classmethod
    # def create(cls,info):
    #     gender,name,year=info.split("-")
    #     current_time=datetime.now().year
    #     age=  current_time-int(year)
    #     return cls(name,age,gender)
    #
    # @staticmethod
    # def is_adult(year):
    #     current_time = datetime.now().year
    #     age = current_time - int(year)
    #     #(age>=18为真，则成年;假，则未成年)
    #     return age>=18
    #
    # @staticmethod
    # def mask_idcard(idcard):
    #     return idcard[:6] + '********' + idcard[-4::]

class Student(Person,Woker):
    def __init__(self,name,age,gender,weight,company,id_card):
        Woker.__init__(self,company)
        super().__init__(name,age,gender,id_card)
        self.weight=weight

    def people(self):
        print(f"我叫{self.name}，年龄{self.age}，性别{self.gender}，重量{self.weight}")
    # def speak(self,msg):
    #     print(f"我叫{self.name}，年龄{self.age}，性别{self.gender}，重量{self.weight},说{msg}")
p1=Student("小影","18","女","60kg","汉堡王","110101199001011234")
p1.id_card="110101199001011231"
print(p1.id_card)
# p1.woker()
# p1.speak("我要说当你的眼睛眯着眼")
# print(isinstance(p1,Person))
# print(isinstance(p1,Student))
# print(issubclass(Student,Person))





# p3=Student("小影","18","女","60kg")
# print(p3.people())
#
# result2=Person.mask_idcard("212101198802030028")
# print(result2)
# result1=Person.is_adult(2009)
# print(result1)
# Person.change("樱桃")
# print(Person.fruits)
#
# p1=Person("李华","16","男")
# p1.gender="女"
# p1.speak("爱吃饭")
# print(p1.__dict__)
# result=Person.create("男-梨花-2004")
# print(result.__dict__)
