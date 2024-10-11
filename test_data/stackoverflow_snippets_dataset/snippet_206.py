# Extracted from https://stackoverflow.com/questions/4028904/what-is-a-cross-platform-way-to-get-the-home-directory
from os.path import expanduser
home = expanduser("~")

from pathlib import Path
home = str(Path.home())

