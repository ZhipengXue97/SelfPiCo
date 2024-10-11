# Extracted from https://stackoverflow.com/questions/6390393/make-tick-labels-font-size-smaller
import matplotlib.pyplot as plt
# We prepare the plot  
fig, ax = plt.subplots()

# We change the fontsize of minor ticks label 
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='minor', labelsize=8)

