
# Inheritance with super Method

class Person:
    def __init__(self,n,age,height,country):
        self.name=n
        self.age=age
        self.height=height
        self.country=country
    def disply(self):
        print('Person Class Instance Method')

class Student(Person):
    def __init__(self,name,age,height,country,roll):
        super().__init__(name,age,height,country)
        self.roll=roll
        print('Student Class Information Constructor Method')
    def student_info(self):
        print(f"Name:{self.name}\nAge:{self.age}\nRoll:{self.roll}")
        self.disply()

s1=Student("Abu Hanif",26,5.6,"Bangladesh",201830625)
s1.student_info()
print()
p1=Person("Taharat",25,5.00,'Bangladesh')
p1.disply()
