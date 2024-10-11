# Extracted from https://stackoverflow.com/questions/3278077/difference-between-getattr-and-getattribute
def __getattr__(self, name):
    return getattr(self._b, name)

