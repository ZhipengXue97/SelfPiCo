# Extracted from https://stackoverflow.com/questions/13694034/is-a-python-list-guaranteed-to-have-its-elements-stay-in-the-order-they-are-inse
a = [[1], [2], [3]]
a[0].append(7)
a
[[1, 7], [2], [3]]

