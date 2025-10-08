class MathOp:
    def add(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            return a+b+c
        elif a is not None and b is not None:
            return a+b
        else :
            return a
m=MathOp()
ans=m.add(2,3,5)
print("a+b+c=",ans)
ans2=m.add(2,7)
print("a+b=",ans2)
ans3=m.add(8)
print("a=",ans3)
