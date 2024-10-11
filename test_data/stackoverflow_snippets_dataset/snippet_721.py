# Extracted from https://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
#!/usr/bin/env python

import subprocess
import sys

result = subprocess.Popen([u'svn', u'info'])
if not callable(getattr(result, "__enter__", None)) and not callable(getattr(result, "__exit__", None)):
    print("foo")
print("bar")

