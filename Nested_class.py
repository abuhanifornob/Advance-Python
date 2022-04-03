# Nested Class

class Army:
    def __init__(self):
        self.name='Abu Hanif'
        self.country='Bangladesh'
        self.gun_object=self.Gun()                                 # Inner Class Object
    def armi_details(self):

        print(f" Armi Name: {self.name}\n Country: {self.country}")
        self.gun_object.show_gun_details()                         # call Gun_detail to inner Class

    class Gun:                                                     # Innner Class dicliaration
        def __init__(self):
            self.name='AK47'
            self.capacity='150 Round'
            self.length='25 fet'
        def show_gun_details(self):
            print(f" Gun name: {self.name} \n Capacity: {self.capacity} \n Length: {self.length}")



a=Army()    #   outer Class Object Create

print(a.name)
print(a.country)
a.armi_details()

gun_object=a.gun_object
gun_object.show_gun_details()

print()

a.armi_details()