# Extracted from https://stackoverflow.com/questions/24988448/how-to-draw-vertical-lines-on-a-given-plot
import matplotlib.pyplot as plt

# x coordinates for the lines
xcoords = [0.1, 0.3, 0.5]
# colors for the lines
colors = ['r','k','b']

for xc,c in zip(xcoords,colors):
    plt.axvline(x=xc, label='line at x = {}'.format(xc), c=c)

plt.legend()
plt.show()

