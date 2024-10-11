# Extracted from https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py
import sys
sys.path.append('../components')
from core import GameLoopEvents

