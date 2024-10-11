# Extracted from https://stackoverflow.com/questions/3451111/unzipping-files-in-python
from zipfile import ZipFile
zf = ZipFile('path_to_file/file.zip', 'r')
zf.extractall('path_to_extract_folder')
zf.close()

