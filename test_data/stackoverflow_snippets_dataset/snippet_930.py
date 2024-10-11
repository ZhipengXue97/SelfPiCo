# Extracted from https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
2656  # peak memory usage (kilobytes on Linux, bytes on OS X)

