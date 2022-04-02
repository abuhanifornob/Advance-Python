class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll

    def exam(self,m):
        self.mark=m
        print(f"Name is:{self.name} Roll:{self.roll} Mark:{self.mark}")

s1=Student('Hanif',25,201830625)
s1.exam(60)

class User:
    @staticmethod
    def show(obj,s,exam_type):
        semister=s
        exam_type=exam_type
        print("name",obj.name)
        print('Age',obj.age)
        print("Roll",obj.roll)
        obj.exam(50)
        print(semister,exam_type)

user1=User()
User.show(s1,'6th','final')




