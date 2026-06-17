import numpy as np

temperatures = [34.2,32.5,31.56,76.78]
total = 0
for temp in temperatures:
    total +=temp
    
avg = total/len(temperatures)
print(avg)    

#now this program cannot be writeen in loops if the dataset is in millions or thounsands therefore we use numpy that can hancdle large dataset efficiently

import numpy as np
temperatures = np.array([34.2,32.5,31.56,76.78])
avg = np.mean(temperatures)
print(avg)

arr1=np.array([1,2,3,4,5])
arr2=np.arange(1,11)
arr3=np.linspace(0,1,5)
arr4=np.zeros((2,3))
arr5=np.ones((2,3))
arr6=np.eye(3)
arr7=np.full((2,3),6)

print("arr1:\n",arr1)
print("arr2:\n",arr2)
print("arr3:\n",arr3)
print("arr4:\n",arr4)
print("arr5:\n",arr5)
print("arr6:\n",arr6)
print(arr7)



arr = np.arange(1,13)
matrix = arr.reshape(3,4)
flat = matrix.ravel()
print("Orignal:\n",arr)
print("Reshaped:\n",matrix)
print("Flattened:",flat)

arr9=np.array([10,20,30,40,50])
mask=arr9>25
filtered=arr9[mask]

print("Mask:",mask)
print("Filtered Values:",filtered)

