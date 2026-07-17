import numpy as np
 
print("-------------------------------")
zero_vector = np.empty(8,dtype=np.int8)     #try int8 int16 int32 int64 float16 to get different result
print(zero_vector,zero_vector.dtype)
print("-------------------------------")
zero_matrix = np.empty((2,2),dtype=np.float16)     #add another bracket when giving dimention 
print(zero_matrix,zero_matrix.dtype)
print("-------------------------------")
zero_tensor = np.empty((3,3,3))    
print(zero_tensor,zero_tensor.dtype)
print("-------------------------------")