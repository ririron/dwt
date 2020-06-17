import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = np.array(Image.open('resource/LENNA.bmp'))

print(im.shape)  #y,xの順

plt.plot(im)
plt.show()

