# Extracted from https://stackoverflow.com/questions/1093322/how-do-i-check-which-version-of-python-is-running-my-script
from sys import version_info 
python_version = f"{version_info.major}.{version_info.minor}"
print(python_version)

