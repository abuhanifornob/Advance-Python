

"""#Exam-1 use class object

class Myclass(object):
    def showInformation(self):
        print("This is firt Coding for advance Tutorial Serice: ")
object1=Myclass()
object1.showInformation()

# Exam 2 not use Class Object

class MyNewClass:
    def showInformation(self):
        print("This is firt Coding for advance Tutorial Serice 2: ")
obj=MyNewClass()
obj.showInformation()


# Example 3.

class Mobile:
    def __init__(self):
        self.mobile='Redme'
    def show(self):
        print("Mobile is: ",self.mobile)

redme=Mobile()
redme.show()
# decliaration
redme.mobile='New Redme'
print(redme.mobile)
redme.show()

"""

# Exam -4

"""class Mobile:
    def __init__(self,m):
        self.mobile_model=m

    def show_mobile_details(self,price):
        self.price=price
        print(f" Mobile Model is:{self.mobile_model} \n Price is: { self.price}")

redmi=Mobile("Redme X")
redmi.show_mobile_details(1000)"""


#  Exam- 5 Memory Allowcation:

class Mobile:
    def __init__(self,m,c,price):
        self.model_name=m
        self.median=c
        self.price=price
    def show_details(self):
        print(f" Model Name: {self.model_name} \n Meadin in: {self.median} \n Price is: {self.price}")

redme=Mobile('Redme','Japan ',1500)
redme.show_details()
print(id(redme))

redmex=Mobile('Redme X','Japan ',1500)
redme.show_details()
print(id(redme))


