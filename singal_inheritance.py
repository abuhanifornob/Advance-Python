# Singal Inheritance......

class Father:
    many=100
    @classmethod
    def show_many(cls):
        print('Class Method -> Father /Supper Class Mony:',cls.many)
    def show_information(self):                      # Instance Method.............
        self.name="Abu Hanif"
        self.country='Bangladesh'
        print(f" Instance Method -> Name:{self.name}\n Country:{self.country}")
    @staticmethod                                        # Static Method
    def static():
        father_name='Nizam Uddin'
        print( ' Static Method -> Father Name: ',father_name)

class Son(Father):                 # Chaild Class
    @classmethod                    # Class method
    def son_method(cls):
        cls.son_name='Tanharun Islam'
        print(cls.son_name)

son=Son()             # Child Object
son.son_method()
son.show_many()
son.static()
son.show_information()

print()

father=Father()

father.show_many()
father.static()
father.show_information()



