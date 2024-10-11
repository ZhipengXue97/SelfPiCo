# Extracted from https://stackoverflow.com/questions/8933237/how-do-i-check-if-a-directory-exists-in-python
import os

if not os.path.isdir("directory_name"):
    os.mkdir("directory_name")

