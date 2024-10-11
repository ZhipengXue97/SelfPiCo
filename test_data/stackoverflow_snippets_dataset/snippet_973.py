# Extracted from https://stackoverflow.com/questions/9885217/in-python-if-i-return-inside-a-with-block-will-the-file-still-close
def example(path, mode):
    with open(path, mode) as f:
        return [line for line in f if condition]

def example(path, mode):
    f = open(path, mode)

    try:
        return [line for line in f if condition]
    finally:
        f.close()

