# Extracted from https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
from pathlib import Path

relative = Path("mydir/myfile.txt")
absolute = relative.absolute()  # absolute is a Path object

from os.path import abspath

absolute = abspath(relative)  # absolute is a str object

