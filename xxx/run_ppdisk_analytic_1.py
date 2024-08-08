import matplotlib.pyplot as plt
from matplotlib import cm
from radmc3dPy import *
import numpy as np

info = np.fromfile('image_analytic.out', sep= ' ', count = 7)
nx, ny = np.int32(info[1:3])
dx, dy = info[4:6]
lam_mic = info[6]

im = np.loadtxt('image_analytic.out', skiprows =6)
im = im.reshape((nx, ny))

f, ax = plt.subplots()
c = ax.imshow(im, vmin = 1e-20, vmax = 3e-17, cmap = 'afmhot')
f.colorbar(c)

im = image.readImage()
image.plotImage(im, vmax=3e-3, au =True, cmap=cm.gist_heat)
