import numpy as np
from PIL import Image

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]

# make a red patch
data[0:3, 0:2] = [255, 200, 200]
data[3:4, 1:4] = [45, 2, 200]
print(data)

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')