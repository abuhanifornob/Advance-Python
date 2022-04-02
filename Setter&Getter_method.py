# Settter & getter Method

class Student:
    def set(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country

s1=Student()
s1.set('Hanif',25,'Bangladesh')
print(s1.name)


