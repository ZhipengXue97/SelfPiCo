# Extracted from https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

indA & indB  # intersection
indA | indB  # union
indA - indB  # difference
indA ^ indB  # symmetric difference

