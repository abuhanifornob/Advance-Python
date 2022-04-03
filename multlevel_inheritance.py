
# multilevel Inheritance

class Father:
    def __init__(self):
        print("Father Class Constructor Method")
    def showF(self):
        print("Father Class Instence Method")
class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor Method")
    def showS(self):
        print("Son Class Instence Method")
class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print("GrandSon class Constructor Method")
    def showGs(self):
        print("Grand Son Class Instence Methos")

grandSonObject=GrandSon()
grandSonObject.showF()
grandSonObject.showS()
grandSonObject.showGs()
print()

sonObject=Son()
sonObject.showF()
sonObject.showS()







