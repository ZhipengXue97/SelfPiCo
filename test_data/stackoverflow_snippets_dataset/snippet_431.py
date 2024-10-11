# Extracted from https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-the-x-or-y-axis
import matplotlib.pyplot as pp
import numpy as np

def resadjust(ax, xres=None, yres=None):
    """
    Send in an axis and I fix the resolution as desired.
    """

    if xres:
        start, stop = ax.get_xlim()
        ticks = np.arange(start, stop + xres, xres)
        ax.set_xticks(ticks)
    if yres:
        start, stop = ax.get_ylim()
        ticks = np.arange(start, stop + yres, yres)
        ax.set_yticks(ticks)

gca().set_ylim(top=new_top) # for example

