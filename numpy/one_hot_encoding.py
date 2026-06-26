import numpy as np
cats = np.array(['red','blue','blue','green','red'])

uniq, inv = np.unique(cats,return_inverse=True)

one_hot = np.eye(len(uniq))[inv]

print("Categories:",uniq)
print("Codes:",inv)
print("One-hot:\n",one_hot.astype(int))

#using sckiti leranr
from sklearn.preprocessing import OneHotEncoder
import numpy as np

cats = np.array(['red','blue','blue','green','red']).reshape(-1,1)

encoder = OneHotEncoder(sparse_output=False)
one_hot = encoder.fit_transform(cats)

print("Categories:", encoder.categories_[0])
print("One-hot:\n", one_hot.astype(int))


