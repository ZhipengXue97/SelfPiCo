# Extracted from https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
from glob import glob
glob("/path/to/directory/*/", recursive = True)

