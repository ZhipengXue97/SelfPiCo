# Extracted from https://stackoverflow.com/questions/1835018/how-to-check-if-an-object-is-a-list-or-tuple-but-not-string
def is_array(var):
    return isinstance(var, (list, tuple))

