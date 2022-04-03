# Hierarchical Inheritance


class Fatehr:
    def __init__(self,name,age,proparty,country):
        self.name=name
        self.age=age
        self.proparty=proparty
        self.country=country
       
    def showF(self):
        print('Fatehr Class Instence Method')

class Son(Fatehr):
    def __init__(self,name,age,proparty,country,son_name):
        super().__init__(name,age,proparty,country)
        self.son_name=son_name
    def showS(self):
        print("Son Class Instence Method")
class Daughter(Fatehr):
    def showD(self):
        print("Daughter Class Instence Method")


son=Son("Nizam Uddin",60,"60 Milions",'Bangladesh','Abu Hanif')
daughter=Daughter("Nizam Uddin",60,"60 Milions",'Bangladesh')
son.showS()



