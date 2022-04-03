# Multiple Inheritance

class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Cnstructor Method")
    def showF(self):
        print("Father Class Instence Method")
class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Class Cnstructor Method")
    def showM(self):
        print("Mother Class Instence Method")
class Son(Mother,Father):
    def __init__(self):
        super().__init__()
        print("Son Class Cnstructor Method")
    def showS(self):
        print("Son Class Instence Method ,Name Is: ")

son=Son()

son.showF()
son.showM()
son.showS()