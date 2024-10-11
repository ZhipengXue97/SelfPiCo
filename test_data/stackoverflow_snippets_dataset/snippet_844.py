# Extracted from https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
hashlib.md5(pathlib.Path('path/to/file').read_bytes()).hexdigest()

