# Extracted from https://stackoverflow.com/questions/32370281/how-to-embed-image-or-picture-in-jupyter-notebook-either-from-a-local-machine-o
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread("your_image.png")
plt.imshow(image)
plt.show()

