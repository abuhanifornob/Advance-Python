# Constructor Ovrritting parameter

class Father:
    def __init__(self,m):
        self.mony=m
        print("Father Class Constructor")
    def instens_method(self):
        self.name='Hanif'
        self.country='Country'
        print('Father Class Insteance Method')

class Son(Father):
    def __init__(self,s):
        self.sone=s
        print('Son Class Constructor ')
    def dis(self):
        print('Son class instance Method')

s=Son('hanif')
s.dis()
print(s.sone)
s.instens_method()

