# Extracted from https://stackoverflow.com/questions/2812520/dealing-with-multiple-python-versions-and-pip
#!/usr/bin/env python3 <-- I changed this line.

# -*- coding: utf-8 -*-
import re
import sys

from pip._internal import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())

