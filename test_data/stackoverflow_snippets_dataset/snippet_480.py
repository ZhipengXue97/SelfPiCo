# Extracted from https://stackoverflow.com/questions/19151/how-to-build-a-basic-iterator
class A(object):
    def __init__(self, l):
        self.data = l

    def __iter__(self):
        return iter(self.data)

In [3]: a = A([2,3,4])

In [4]: [i for i in a]
Out[4]: [2, 3, 4]

