# Extracted from https://stackoverflow.com/questions/107705/disable-output-buffering
_orig_print = print

def print(*args, **kwargs):
    _orig_print(*args, flush=True, **kwargs)

print = functools.partial(print, flush=True)

