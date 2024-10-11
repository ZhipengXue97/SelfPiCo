# Extracted from https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-directory-possibly-including-intermediate-directories
from pathlib import Path
Path("path/with/childs/.../").mkdir(parents=True, exist_ok=True)

