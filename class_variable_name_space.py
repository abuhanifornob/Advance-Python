# Class Variable Name Space

class Mobile:
    good_performance='Yes'           # Class Variable Declearation

    def __init__(self):              # Instance Method
        self.mobile_name='Sony'      #

    def show_name(self):
        print(self.show_name())

    @classmethod
    def class_method(cls):
        print(cls.good_performance)

# 3 Object Create
redme=Mobile()
redmeX=Mobile()
redmeMX=Mobile()

print(Mobile.good_performance)   #Yes
print(redme.good_performance)    # Yes
print(redmeX.good_performance)   # Yes
print(redmeMX.good_performance)  # Yes

# Modify Class variabel by the Class Name
Mobile.good_performance="NO"
print()
print(Mobile.good_performance)   # NO
print(redme.good_performance)    # NO
print(redmeX.good_performance)   # NO
print(redmeMX.good_performance)  # NO
print()
# Modify Class Variable by the Class Object

redme.good_performance='Good Work Performance'
print(Mobile.good_performance)   # NO
print(redme.good_performance)    # Good Work Performance
print(redmeX.good_performance)   # NO
print(redmeMX.good_performance)  # NO

print()

print(Mobile.class_method())