import numpy as np

print("-------------------------------")
zero_vector = np.zeros(8,dtype=np.int64)     #make zero matrics and tensor
print(zero_vector,zero_vector.dtype)
print("-------------------------------")
zero_matrix = np.zeros((2,2),dtype=np.float16)     #add another bracket when giving dimention 
print(zero_matrix,zero_matrix.dtype)
print("-------------------------------")
zero_tensor = np.zeros((3,3,3))    
print(zero_tensor,zero_tensor.dtype)
print("-------------------------------")



