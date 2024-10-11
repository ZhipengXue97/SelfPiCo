# Extracted from https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
import sys
from pathlib import Path
path_file = Path(sys.path[0])
print(path_file)

