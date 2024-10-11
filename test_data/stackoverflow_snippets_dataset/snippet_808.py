# Extracted from https://stackoverflow.com/questions/12998430/how-to-remove-xticks-from-a-plot
plt.gca().axes.xaxis.set_ticklabels([])
plt.gca().axes.yaxis.set_ticklabels([])
plt.grid(alpha = 0.2)

