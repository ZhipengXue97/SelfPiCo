# Extracted from https://stackoverflow.com/questions/1158076/implement-touch-using-python
def touch(fname):
    open(fname, 'a').close()
    os.utime(fname, None)

