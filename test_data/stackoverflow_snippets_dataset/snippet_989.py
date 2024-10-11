# Extracted from https://stackoverflow.com/questions/11887762/how-do-i-compare-version-numbers-in-python
import sys
needs = (3, 9) # or whatever
pvi = sys.version_info.major, sys.version_info.minor    

try:
    assert pvi >= needs
except:
    print("will fail!")
    # etc.

