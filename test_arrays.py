import numpy as np
import PIL.Image
import matplotlib.pyplot as plt


# make arrays for images
def make_arrays():
    x = np.arange(-5, 5, 1)
    y = np.arange(-5, 5, 1)
    #z = np.arange(-1, 1, 1)
    z = 0.1
    xx, yy, zz = np.meshgrid(x, y, z, sparse=True)
    #f = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
    g = .01
    import pdb; pdb.set_trace()
    f = np.sin(g*xx)*np.cos(g*yy)+np.sin(g*yy)*np.cos(g*zz)+np.cos(g*xx)*np.sin(g*zz)
    h = plt.contourf(x,y,f)
    plt.show()


def start_show():
    import pycrafter6500
    images = []
    # images.append((numpy.asarray(PIL.Image.open("testimage.tif"))//129))

    images.append((np.asarray(PIL.Image.open("testimage.tif"))//129))

    dlp=pycrafter6500.dmd()

    dlp.stopsequence()

    dlp.changemode(3)

    exposure=[1000000]*30
    dark_time=[0]*30
    trigger_in=[False]*30
    trigger_out=[1]*30

    dlp.defsequence(images,exposure,trigger_in,dark_time,trigger_out,0)

    dlp.startsequence()


make_arrays()