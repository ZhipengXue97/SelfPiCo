# Extracted from https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output

import os

filename = "/foo/bar/baz.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write("FOOBAR")


from pathlib import Path
output_file = Path("/foo/bar/baz.txt")
output_file.parent.mkdir(exist_ok=True, parents=True)
output_file.write_text("FOOBAR")

import os
import errno

filename = "/foo/bar/baz.txt"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

with open(filename, "w") as f:
    f.write("FOOBAR")


