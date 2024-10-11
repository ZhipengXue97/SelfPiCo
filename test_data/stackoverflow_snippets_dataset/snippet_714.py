# Extracted from https://stackoverflow.com/questions/14507591/python-dictionary-comprehension
i_s = range(1, 11)
x_s = range(1, 11)
# x_s = range(11, 1, -1) # Also works
d = dict([(i_s[index], x_s[index], ) for index in range(len(i_s))])

