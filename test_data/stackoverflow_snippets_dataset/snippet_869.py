# Extracted from https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
# create a subplot with 2 rows and 1 columns
fig, ax = plt.subplots(2,1)

fig = plt.figure() # create the canvas for plotting
ax1 = plt.subplot(2,1,1) 
# (2,1,1) indicates total number of rows, columns, and figure number respectively
ax2 = plt.subplot(2,1,2)

# for example, sharing x-axis, y-axis for all subplots can be specified at once
fig, ax = plt.subplots(2,2, sharex=True, sharey=True)

