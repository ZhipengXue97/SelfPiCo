# Extracted from https://stackoverflow.com/questions/2104080/how-do-i-check-file-size-in-python
# f is a file-like object. 
f.seek(0, os.SEEK_END)
size = f.tell()

# f is a file-like object. 
old_file_position = f.tell()
f.seek(0, os.SEEK_END)
size = f.tell()
f.seek(old_file_position, os.SEEK_SET)

