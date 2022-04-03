# constructor Inheritance

class Father:
    def __init__(self):
        self.mony=500
        print('Fathers class Constructior')
    def show(self):
        print('Father Class Instance Method')
class Son(Father):
    def disp(self):
        print("Son class Instance")

son=Son()
print(son.mony)
son.disp()
son.show()