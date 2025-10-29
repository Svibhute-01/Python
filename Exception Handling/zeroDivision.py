no1=int(input("Enter No1 :"))
no2=int(input("Enter NO2:"))
try:
    ans=no1//no2
except ZeroDivisionError:

    print("ZeroDivisionError:Can not divide by zero!")
else:
    print("Division is:",ans)
finally:
    print("Code executed succesfully...")