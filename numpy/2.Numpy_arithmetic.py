import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)
print(array1 % array2)

scores= np.array([91,55,100,73,92,64])
print(scores == 100)

scores[scores < 60] = 0
print(scores)

array=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.argmin(array))

print(np.sum(array, axis=0))

matrix=np.array([[1,2,3,4],[4,5,6,7]])
vector=np.array([10,20,30,0])
result=matrix + vector
print(result)

col=np.array([[1],
              [2],
              [3]])

rol=np.array([10,20,30])
result=col + rol
print(result)

import numpy as np
adesh = np.array([[[1,2,3,4],
                 [4,5,6,8]]])
print(adesh.shape)
print(adesh.ndim)
print(adesh.dtype)

#converting data type
 
import numpy as np
arr = np.array([2.5,3.69,68.7,96.80])
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)