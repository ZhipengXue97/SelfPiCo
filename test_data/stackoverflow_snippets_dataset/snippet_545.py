# Extracted from https://stackoverflow.com/questions/432112/is-there-a-numpy-function-to-return-the-first-index-of-something-in-an-array
other_array[first_array == item]

a = numpy.arange(100)
other_array[first_array > 50]

index = numpy.nonzero(first_array == item)[0][0]

