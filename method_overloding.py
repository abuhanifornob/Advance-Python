

# Python does not support method overloding by default. But there are different ways to achive method
#Overloding in Python

# method One1

from multipledispatch import dispatch
class Calculator:
    # method One1
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            ans=a+b+c
            return ans
        elif a!=None and b!=None:
            ans=a+b
            return ans
        else:
            print("more then one Argument for Sum")
            return a

    # method Two.......................

    def addAnyArgument(self,datatype,*args):
        answer=1
        # if datatype is int
        # initialize answer as 0
        if datatype=='int':
            answer = 0
        # if datatype is str
        # initialize answer as ''
        if datatype=='atr':
            answer=''
        # Traverse through the arguments
        for x in args:
            # This will do addition if the
            # arguments are int. Or concatenation
            # if the arguments are str
            answer=answer+x
        return answer

    # method Three.......................

    from multipledispatch import dispatch
    @dispatch(int,int)
    def product(self,frist,second):
        result=frist*second
        return result;

    @dispatch(int,int,int)
    def product(self,frist,second,thred):
        result=frist*second*thred
        return result

    @dispatch(float,float,float)
    def product(self,frist,second,thred):
        result = frist * second * thred
        return result





cal=Calculator()
print(cal.add(10))
print("summiation is: )",cal.addAnyArgument('int',12,12,12,12))


print("Product:",cal.product(2.0,3.0,3.0))
print("Product:",cal.product(2,3,3))


# method One2
