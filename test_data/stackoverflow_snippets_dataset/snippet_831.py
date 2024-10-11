# Extracted from https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
import six

# OK
if six.PY2:
  x = it.next() # Python 2 syntax
else:
  x = next(it) # Python 3 syntax

# Better
x = six.next(it)

