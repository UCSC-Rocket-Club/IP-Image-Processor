from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
from scipy.misc import imsave
import numpy as np

f = misc.imread('export.png', mode='I')

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1


# print(im)
# print(f)

sx = ndimage.sobel(f, axis=0, mode='constant')
sy = ndimage.sobel(f, axis=1, mode='constant')
sob = np.hypot(sx, sy)


print(sob)

# target = open("sx.txt", 'w')


# for i in range(0, len(sx)):
# 	for j in range(0, len(sx[i])):
# 		target.write(str(sx[i][j]) + ",")

# target = open("sy.txt", 'w')

# for i in range(0, len(sy)):
# 	for j in range(0, len(sy[i])):
# 		target.write(str(sy[i][j]) + ",")


plt.imshow(sob)
plt.axis('off')
plt.show()

plt.imshow(f)
plt.axis('off')
plt.show()

