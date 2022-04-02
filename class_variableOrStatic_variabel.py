#  Class Variabel or Static Variable with Class Method


class Company:
    section='It'                   # Class Variable

    def __init__(self):            # Instance Method
        self.section_s='sewing'    # Instance Variable

    def show_section(self):         # Instance Method
        print(self.section_s)       # Accessing Instance Variable

    @classmethod
    def show(cls):                   # Class Method
        print(cls.section)           # Accessecing Class Variable

obj1=Company()
print("Call by Objec",obj1.section)
print("Call by Class ",Company.section)

obj1.section='No'

print("Call by Objec",obj1.section)
print("Call by Class ",Company.section)

"""Company.section_it='Change by Class Name'"""
print("Call by Objec",obj1.section)
print("Call by Class ",Company.section)

obj1.show()


obj1.show_section()