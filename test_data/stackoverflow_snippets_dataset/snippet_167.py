# Extracted from https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
array = [0, 10, 20, 40]
[array[~i] for i, _ in enumerate(array)]
[40, 20, 10, 0]

