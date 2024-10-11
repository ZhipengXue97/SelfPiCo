# Extracted from https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
#importing the libraries
from PIL import Image
import numpy as np

data = np.load('/kaggle/input/objects-dataset/nmbu.npy')
im = Image.fromarray(data, 'RGB')
#saving the image from the npy format
im.save("your_file.jpeg")

