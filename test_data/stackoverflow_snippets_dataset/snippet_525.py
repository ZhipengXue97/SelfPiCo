# Extracted from https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
def anyitem(iterable):
    try:
        return iter(iterable).next()
    except StopIteration:
        return None

