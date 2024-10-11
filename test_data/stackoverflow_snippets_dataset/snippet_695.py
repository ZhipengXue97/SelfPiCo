# Extracted from https://stackoverflow.com/questions/2176424/hiding-axis-text-in-matplotlib-plots
frame1 = plt.gca()
frame1.axes.xaxis.set_ticklabels([])
frame1.axes.yaxis.set_ticklabels([])

