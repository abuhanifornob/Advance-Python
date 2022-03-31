# without passing parametar

"""class Laptop:
    def __init__(self):
        print("Autometic Run instance Method ")
ph=Laptop()"""


class Laptop:
    def __init__(self,model,medain='Bangladesh'):
        self.model=model
        self.medain=medain
    def show(self,p):
        price=p
        print(f"Model Name:{self.model}\nMedain : {self.medain} \n price is:{ price} ")

hp=Laptop('vv15')
hp.show(1000)
print()
hp=Laptop('bb15','india')
hp.show(1200)