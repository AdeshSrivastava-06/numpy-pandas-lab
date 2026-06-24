import numpy as np

arr=np.array([10,20,30,40,50])
print(arr[3])
print(arr[-1])
print(arr[::2])
print(arr[1:4:2])
print(arr[::-1]) #reverse

#fancy indexing
print(arr[0,2,3])

#reshaping 
"""reshaping always returns a view not a copy
reshape(rows,columns) specify new shape if dimension match"""

import numpy as np

arr=np.array([1,2,3,4,5,6])
reshaped_arr=arr.reshape(2,3)
print(reshaped_arr)
print(arr)

""" flatten convert 2d 3d to 1d consist of ravel()->views orignal array affected
flatten()->copy orignal array not affected"""

import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())

"""inserting a element in array
np.insert(array,index,value,axis=NONE(flatten))
axis=0 row-wise
axis=1 col-wise" never changes the original array"""

import numpy as np

arr=np.array([10,20,30,40,50,60])
print(arr)
new_arr=np.insert(arr,2,100,axis=0)
print(new_arr)

#insert in 2D
import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
#insert a new row at index 1
new_arr2d=np.insert(arr,1,[5,6,8],axis=0)
print(new_arr2d)

#append
import numpy as np
arr=np.array([10,20,30])
new_arr=np.append(arr,[199,99])
print(new_arr)

arr = np.array([[1,2,3],[65,66,77]])
print(np.append(arr,[[10,20,30]],axis=0))

arr = np.array([[1,2,3],
                [65,66,77]])

new = np.append(arr, [[99],[99]], axis=1)

print(new)




""" np.concatenate((arr1,arr2),axis=0)
axid=0 vertical stacking
axis=1 horizontal stacking"""

import numpy as np

arr1=np.array([[1,2,3]])
arr2=np.array([[4,5,6]])

new_arr=np.concatenate((arr1,arr2),axis=0)
print(new_arr)

"""np.delete(array,index,axis=NONE)
flatten array"""

import numpy as np
arr=np.array([10,20,30,40,50])
new_arr=np.delete(arr,0)
print(new_arr)

arr_2d = np.array([[1,2,3],[4,5,6]])
new_arr_2d=np.delete(arr_2d,[0],axis=0)
print(new_arr_2d)


"""vstack() row stack
hstack() column wise"""

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

"""np.split() equal, np.hsplit(), np.vsplit()"""
import numpy as np
arr=np.array([10,20,30,40,50,60])
print(np.split(arr,3))

arr2=np.array([[20,30,50,90,77,54],
               [78,54,69,99,66,23]])
print(np.vsplit(arr2,2))
print(np.hsplit(arr2,3))
