# Extracted from https://stackoverflow.com/questions/3584805/what-does-the-argument-mean-in-fig-add-subplot111
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.subplot(3,2,1)
plt.subplot(3,2,3)
plt.subplot(3,2,5)
plt.subplot(2,2,2)
plt.subplot(2,2,4)

