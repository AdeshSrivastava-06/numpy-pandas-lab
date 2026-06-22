import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img=Image.open("sample.jpg")
imp_array=np.array(img)

gray_img = np.dot(imp_array[...,:3],[0.29,0.586,0.1140])
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.title("Orignal")
plt.imshow(imp_array)
plt.show()

plt.subplot(1,2,1)
plt.title("Grayscale")
plt.imshow(gray_img,cmap="gray")

plt.show(block=True)
