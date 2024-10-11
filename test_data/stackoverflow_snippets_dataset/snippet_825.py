# Extracted from https://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
zip(range(5), xrange(100000000))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

