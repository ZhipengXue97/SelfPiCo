# Extracted from https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
[[1] * 4] * 3

[[1, 1, 1, 1]] * 3

inner = [1,1,1,1]
outer = [inner]*3
outer
[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
inner[0] = 5
outer
[[5, 1, 1, 1], [5, 1, 1, 1], [5, 1, 1, 1]]

