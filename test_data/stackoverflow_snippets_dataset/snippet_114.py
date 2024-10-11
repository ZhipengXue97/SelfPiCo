# Extracted from https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python
import os
print(os.path.splitext("/path/to/some/file.txt")[0])


import os
print(os.path.splitext("/path/to/some/file.txt.zip.asc")[0])


