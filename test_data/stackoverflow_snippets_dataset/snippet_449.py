# Extracted from https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
import more_itertools as mit


text = "supercalifragilisticexpialidocious"
search = lambda x: x == "i"

list(mit.locate(text, search))
# [8, 13, 15, 18, 23, 26, 30]

