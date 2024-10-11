# Extracted from https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
import os
from contextlib import suppress

with suppress(OSError):
    os.remove(filename)

