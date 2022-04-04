
# Method Overriding

#define parent class
class Parent:
    #constructor method
    def __init__(self):
        self.value='Inside Parent'
    # Show's parent method
    def show(self):
        print(self.value)

#define child class
class Child(Parent):
    #constructor method
    def __init__(self):
        self.value='Inside Child'
    #show's child method
    def show(self):
        print(self.value)

#drives code
obj1=Child()
obj1.show()

obj2=Parent()
obj2.show()


# Method overriding with multiple inheritance

#define parent1 class
class Father:
    # Constructor method
    """def __init__(self):
        self.value='Inside Parent 1'
    # parent1 Show's Method"""
    def disply(self):
        print('inside Parent 2')

#define parent2 class
class Mother:
    # Constructor method
    """def __init__(self):
        self.value='Inside Parent 2'"""
    # parent1 Show's Method
    def show(self):
        print(self.value)

#define Child Class With multiple Inheritance
class Child(Father,Mother):
    #constructor Method
    """def __init__(self):
        self.value='Inside Child Class'"""
    # Childs Show's Methods.
    def show(self):
        print("Inside Chhild ")

print("Multiple inheritance with method Overriding")
c=Child()
c.show()
c.disply()


# Python program to demonstrate
# overriding in multilevel inheritance


# Python program to demonstrate
# overriding in multilevel inheritance


class Parent():

    # Parent's show method
    def display(self):
        print("Inside Parent")


# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):

    # Child's show method
    def show(self):
        print("Inside Child")


# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):

    # Child's show method
    def show(self):
        print("Inside GrandChild")


# Driver code
print()
print('overriding in multilevel inheritance')
g = GrandChild()
g.show()
g.display()

# Python program to demonstrate
# calling the parent's class method
# inside the overridden method
class Parent:
    def show(self):
        print("Inside Parent Class")
class Child(Parent):
    def show(self):
        Parent.show(self)
        print("Inside Child Class")
# derive code
print()
print('.....')
obj1=Child()
obj1.show()


# Python program to demonstrate
# calling the parent's class method
# inside the overridden method
# super Method Use

class Parent:
    def show(self):
        print("Inside Parent Class")
class Child(Parent):
    def show(self):
        super().show()
        print("Inside Child Class")
# derive code
print()
print('Super() Use')
obj1=Child()
obj1.show()

class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GFG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)

# class GFG2 inherit Class GFG1
class GFG2(GFG1):
    def __init__(self):
        super().__init__()
        print('HEY !!!!!! GfG I am initialised(Class GFG2)')

    def sub_GFG(self, b):
        super().sub_GFG(b + 1)
        print('Printing from class GFG2:', b)

# class GFG3 inherit Class GFG2
class GFG3(GFG2):
    def __init__(self):
        super().__init__()
        print('HEY !!!!!! GfG I am initialised(Class GFG3)')

    def sub_GFG(self, b):
        super().sub_GFG(b+1)
        print('Printing from class GFG3:', b)

obj=GFG3()
obj.sub_GFG(10)

print()

#define parent1 class
class Father:
    # Constructor method
    """def __init__(self):
        self.value='Inside Parent 1'
    # parent1 Show's Method"""
    def show(self):
                print('inside Parent 1')

#define parent2 class
class Mother:
    # Constructor method
    """def __init__(self):
        self.value='Inside Parent 2'"""
    # parent1 Show's Method
    def show(self):
        print('Inside Parent-2')

#define Child Class With multiple Inheritance
class Child(Father,Mother):
    #constructor Method
    """def __init__(self):
        self.value='Inside Child Class'"""
    # Childs Show's Methods.
    def show(self):
        Father.show(self)
        Mother.show(self)
        print("Inside Chhild ")

print("Multiple inheritance with method Overriding")
c=Child()
c.show()




