prices = [100,200,300]

discount = 10
final_prices = []
for price in prices:
    final_price = price - (price*discount/100)
    final_prices.append(final_price)
    
print(final_prices)    

"""broadcasting"""
import numpy as np
prices = np.array([100,200,300])
discount = 10 #scaler
final_prices = prices - (prices*discount/100)
print(final_prices)

"""vectorization"""

list1 = [1,2,3]
list2 = [4,5,6]

result = [x+y for x,y in zip(list1,list2)]
print(result)

#fast approcah
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1+arr2)

"""handling missing values 3 functiosn are usefull
np.isnan-> detect missing values
np.nan_to_num()
np.isinf()
"""

import numpy as np

arr=np.array([1,2,np.nan,5,6])
print(np.isnan(arr))

"""replacing NAN value np.nan_to_num(array,nan=value)  default=0"""

import numpy as np

arr=np.array([1,2,np.nan,5,6])
clean_arr = np.nan_to_num(arr,nan=22)
print(clean_arr)

"""np.isinf() used for infinity vaues"""
import numpy as np
arr = np.array([2,5,3,np.inf,77,-np.inf])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr,posinf=66,neginf=55)
print(cleaned_arr)