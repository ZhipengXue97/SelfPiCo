# Extracted from https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
import os
import tempfile

path = tempfile.mktemp(dir=path)
os.makedirs(path)
os.rmdir(path)

