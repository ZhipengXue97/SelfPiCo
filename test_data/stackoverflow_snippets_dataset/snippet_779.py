# Extracted from https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields
def props(x):
    return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))

