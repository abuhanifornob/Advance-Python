# Instance variabel

class Mobile:
    def __init__(self):
        self.mobile_bame='Redmi'
    def show(self):
        print(self.mobile_bame)    #  accessing Instance Variabe

model=Mobile()
model1=Mobile()
model2=Mobile()

print(model.mobile_bame)
print(model1.mobile_bame)
print(model2.mobile_bame)

model1.mobile_bame='Redmi 6'

print()
print(model.mobile_bame)
print(model1.mobile_bame)
print(model2.mobile_bame)