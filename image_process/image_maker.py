# pip install pillow
# pip install numpy 

import numpy as np
from PIL import Image

array = np.array(
[[0, 255, 255, 255, 0], 
[255, 0, 0, 100, 255],
[255, 0, 100, 100, 255], 
[0, 225, 225, 255, 255], 
[0, 0, 0, 100, 255],
[0, 0, 100, 100, 255],
[0, 100, 255, 255, 0]], dtype=np.uint8)
print(array)

im = Image.fromarray(array)
im.save("image_process/number_img/9.jpg")