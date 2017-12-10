from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
from scipy.misc import imsave
import numpy as np

f = misc.imread('export.png', mode='I')

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1

print(im)
target = open("im.txt", 'w')

for i in range(0, len(im)):
	for j in range(0, len(im[i])):
		target.write(str(im[i][j]) + ",")
	target.write("\n")

# # print(im)
# # print(f)

# sx = ndimage.sobel(f, axis=0, mode='constant')
# sy = ndimage.sobel(f, axis=1, mode='constant')
# sob = np.hypot(sx, sy)


# print(sob)

# target = open("sob.txt", 'w')


# for i in range(0, len(sob)):
# 	for j in range(0, len(sob[i])):
# 		target.write(str(sob[i][j]) + ",")
# 	target.write("\n")

# target = open("export.txt", 'w')

# for i in range(0, len(f)):
# 	for j in range(0, len(f[i])):
# 		target.write(str(f[i][j]) + ",")
# 	target.write("\n")


# plt.imshow(sx)
# plt.axis('off')
# plt.show()

# plt.imshow(sy)
# plt.axis('off')
# plt.show()

# plt.imshow(sob)
# plt.axis('off')
# plt.show()

# plt.imshow(f)
# plt.axis('off')
# plt.show()

