# Extracted from https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
def f():
    if not hasattr(f, 'value'):
        setattr(f, 'value', singletonvalue)
    return f.value

