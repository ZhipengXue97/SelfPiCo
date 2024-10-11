# Extracted from https://stackoverflow.com/questions/9295026/how-to-remove-axis-legends-and-white-padding
import matplotlib.pyplot as plt
import numpy as np

def make_image(data, outputname, size=(1, 1), dpi=80):
    fig = plt.figure()
    fig.set_size_inches(size)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.set_cmap('hot')
    ax.imshow(data, aspect='equal')
    plt.savefig(outputname, dpi=dpi)

# data = mpimg.imread(inputname)[:,:,0]
data = np.arange(1,10).reshape((3, 3))

make_image(data, '/tmp/out.png')

