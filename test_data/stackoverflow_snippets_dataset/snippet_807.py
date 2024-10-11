# Extracted from https://stackoverflow.com/questions/4978738/is-there-a-python-equivalent-of-the-c-sharp-null-coalescing-operator
def default_val(expr, default=None):
    try:
        tmp = expr()
    except Exception:
        tmp = default
    return tmp

default_val(lambda: some['complex'].expression('with', 'possible')['exceptions'], '')

