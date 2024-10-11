# Extracted from https://stackoverflow.com/questions/67631/how-can-i-import-a-module-dynamically-given-the-full-path
import sys
sys.path.append("<project-path>/lib/")
from tes1 import Client1
from tes2 import Client2
import tes3

from test import Client1
from test import Client2
from test import test3

