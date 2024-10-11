# Extracted from https://stackoverflow.com/questions/14770735/how-do-i-change-the-figure-size-with-subplots
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#generate random data
x,y=range(100), range(10)
z=np.random.random((len(x),len(y)))
Y=[z[i].sum() for i in range(len(x))]
z=pd.DataFrame(z).unstack().reset_index()

#Plot data
fig, axs = plt.subplots(2,1,figsize=(16,9), gridspec_kw={'height_ratios': [1, 2]})
axs[0].plot(Y)
axs[1].scatter(z['level_1'], z['level_0'],c=z[0])

