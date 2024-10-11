chunk_size = None
if not isinstance(chunk_size, int):
    raise TypeError("chunk_size must be an int, it is instead a %s." % type(chunk_size))