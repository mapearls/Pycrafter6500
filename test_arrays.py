import numpy as np
import PIL.Image
import matplotlib.pyplot as plt


# make arrays for images
def make_arrays():
    x = np.arange(-5, 5, .01)
    y = np.arange(-5, 5, .01)
    #z = np.arange(-5, 5, .
    z = 0.3
    xx, yy = np.meshgrid(x, y, sparse=True)
    #f = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
    g = 1
    # f = np.sin(g*xx)*np.cos(g*yy)+np.sin(g*yy)*np.cos(g*zz)+np.cos(g*xx)*np.sin(g*zz)
    f = (np.sin(g * xx) * np.cos(g * yy)) + (np.sin(g * yy) * np.cos(g * z) )+ (np.cos(g * xx) * np.sin(g * z))

    h = plt.contourf(x, y, f)
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