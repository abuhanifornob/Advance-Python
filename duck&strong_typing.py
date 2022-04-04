# Dauck Typing & Strong Typing

class Duck:
    def walk(self):
        print('thapak thapak thapak thapak')
class Horse:
    def walk(self):
        print('thabdak thabdak thabdak thabdak')
class Cat:
    def talk(self):
        print('Meow Meow Meow Meow')

def myFunction(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    elif hasattr(obj,'talk'):
        obj.talk()

d=Duck()
myFunction(d)

h=Horse()
myFunction(h)
c=Cat()
myFunction(c)