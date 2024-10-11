# Extracted from https://stackoverflow.com/questions/7125009/how-to-change-legend-fontsize-with-matplotlib-pyplot
import pylab as plot
params = {'legend.fontsize': 20,
          'legend.handlelength': 2}
plot.rcParams.update(params)

