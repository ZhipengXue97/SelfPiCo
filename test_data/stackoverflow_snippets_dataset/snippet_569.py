# Extracted from https://stackoverflow.com/questions/30418481/error-dict-object-has-no-attribute-iteritems
try:
    iteritems
except NameError:
    iteritems = items

