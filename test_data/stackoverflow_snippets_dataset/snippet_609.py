# Extracted from https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import
from itertools import count

import foo
foo.count()

import itertools

import foo
foo.itertools.count()

