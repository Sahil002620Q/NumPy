import numpy as np
vector = np.array([0])

matrix = np.array([[0,1],[1,0]],dtype=np.int16)

tensor = np.array([[[0,0,0],[1,1,1],[1,1,0]],[[1,0,0],[0,1,0],[0,0,1]]])

print(vector)
print("dimention :",vector.ndim)
print("size : ",vector.size)
print("type : ",vector.dtype)
print("")
print()
print(matrix)
print("dimention :",matrix.ndim)
print("size : ",tensor.size)
print("type : ",tensor.dtype)
print("")
print()
print(tensor)
print("dimention :",tensor.ndim)
print("size : ",tensor.size)
print("type : ",tensor.dtype)
print("")
print()

l = [1,2]
print(type(matrix))





