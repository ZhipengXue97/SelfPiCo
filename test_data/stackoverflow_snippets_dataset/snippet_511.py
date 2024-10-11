# Extracted from https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
import os
import re
from pathlib import Path

for f in os.listdir(training_data_dir2):
  for file in os.listdir( training_data_dir2 + '/' + f):
    oldfile= Path(training_data_dir2 + '/' + f + '/' + file)
    newfile = Path(training_data_dir2 + '/' + f + '/' + file[49:])
    p=oldfile
    p.rename(newfile)

