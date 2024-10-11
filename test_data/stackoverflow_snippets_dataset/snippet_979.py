# Extracted from https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
import re
import os

dir_name = "."
files = [os.path.join(dir_name, f) for f in os.listdir(dir_name) if re.match(r'.*\.(jpg|jpeg|png)', f)]

