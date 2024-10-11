# Extracted from https://stackoverflow.com/questions/406121/flattening-a-shallow-list-in-python
from itertools import chain
list(chain.from_iterable(mi.image_set.all() for mi in h.get_image_menu()))

