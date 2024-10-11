# Extracted from https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
import zipfile
from pathlib import Path
with zipfile.ZipFile("archive.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for path in Path("include_all_of_this_folder").rglob("*"):
        zf.write(path, path.as_posix())

