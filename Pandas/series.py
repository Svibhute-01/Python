import pandas as pd

a=[1,2,3,4]
myvar=pd.Series(a)
print(myvar)

a=["Snehal","Shruti","Saniya","Nilam"]
print(pd.Series(a,index=["a","b","c","d"]))