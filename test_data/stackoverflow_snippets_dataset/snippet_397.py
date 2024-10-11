# Extracted from https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
# iteration disregarding content
sum(1 for _ in some_iterable)
# unpacking disregarding specific elements
head, *_ = values
# function disregarding its argument
def callback(_): return True

42
42
f'the last answer is {_}'
'the last answer is 42'
_
'the last answer is 42'
_ = 4  # shadow ``builtins._`` with global ``_``
23
23
_
4

