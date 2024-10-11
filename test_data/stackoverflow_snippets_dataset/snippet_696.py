# Extracted from https://stackoverflow.com/questions/1592565/determine-if-variable-is-defined-in-python
try:
    a # does a exist in the current namespace
except NameError:
    a = 10 # nope

