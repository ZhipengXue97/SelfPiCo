# Extracted from https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size
import matplotlib.pyplot as plt

# set up a plot with dummy data
fig, ax = plt.subplots()
x = [0, 1, 2]
y = [0, 3, 9]
ax.plot(x,y)

# title and labels, setting initial sizes
fig.suptitle('test title', fontsize=12)
ax.set_xlabel('xlabel', fontsize=10)
ax.set_ylabel('ylabel', fontsize='medium')   # relative to plt.rcParams['font.size']

# setting label sizes after creation
ax.xaxis.label.set_size(20)
plt.draw()

