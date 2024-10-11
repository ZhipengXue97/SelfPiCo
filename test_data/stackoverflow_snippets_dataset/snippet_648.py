# Extracted from https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy
import numpy as np
csv = np.genfromtxt('test.csv', delimiter=",")
print(csv)

