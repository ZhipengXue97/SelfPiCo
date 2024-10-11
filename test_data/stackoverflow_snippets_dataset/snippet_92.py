# Extracted from https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
import os
filename, file_extension = os.path.splitext('/path/to/somefile.ext')
filename
'/path/to/somefile'
file_extension
'.ext'

os.path.splitext('/a/b.c/d')
('/a/b.c/d', '')
os.path.splitext('.bashrc')
('.bashrc', '')

