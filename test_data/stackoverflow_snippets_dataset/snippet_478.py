# Extracted from https://stackoverflow.com/questions/6591931/getting-file-size-in-python
import os

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

