# Extracted from https://stackoverflow.com/questions/2361426/get-the-first-item-from-an-iterable-that-matches-a-condition
next(i for i in range(100000000) if i == 1000)

next(filter(lambda i: i == 1000, range(100000000)))

next(filter(lambda i: i == 1000, range(100000000)), False)

next((i for i in range(100000000) if i == 1000), False)

