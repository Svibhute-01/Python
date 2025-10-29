import numpy as np

Arr1=np.array([1,2,3,4,5,6])
Arr2=np.array([[1,2,3],[4,5,6]])
Arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(Arr1,"\n",Arr2,"\n",Arr3)

print("Shape:",Arr1.shape,"Dimension:", Arr1.ndim,"Size:",Arr1.size,"Datatype:",Arr1.dtype)



reshaped = Arr1.reshape(2,3)
print("Reshaped Array 1:")
print(reshaped)

print("Shape:",Arr2.shape,"Dimension:", Arr2.ndim,"Size:",Arr2.size,"Datatype:",Arr2.dtype)
print("Shape:",Arr3.shape,"Dimension:", Arr3.ndim,"Size:",Arr3.size,"Datatype:",Arr3.dtype)
