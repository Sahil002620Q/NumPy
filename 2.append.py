import numpy as np 

vector = np.array([1,2,3])
print(vector)
print(vector[0])
print(vector[1])
print(vector[2])
try:
    print(vector[3])
except IndexError:
    print("Index error : exceeded length of array")

#addition : to add elements in np array there is no direct way , and we can only add new elements in nev variable who will store both old + new


# batch opt
vector_main = np.array([1,2,3,4,5])
vector_mod = np.append(vector_main,[11])   # if vector,element then vector first elenet at last of list 
vector_mod2 = np.append([11],vector_main)   # if element,vector then element first then vector at last in new vector
print(vector_mod)
print(vector_mod2)

#modify particular element by index                         
vector_main[1] = 22
vector_main[3] = 44

print(vector_main)



#slice