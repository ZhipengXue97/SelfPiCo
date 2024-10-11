# Extracted from https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
@contextlib.contextmanager
def packageResource():
    class Package:
        ...
    package = Package()
    yield package
    package.cleanup()

class Package(object):
    def __new__(cls, *args, **kwargs):
        @contextlib.contextmanager
        def packageResource():
            # adapt arguments if superclass takes some!
            package = super(Package, cls).__new__(cls)
            package.__init__(*args, **kwargs)
            yield package
            package.cleanup()

    def __init__(self, *args, **kwargs):
        ...

class Package(object):
    def __new__(cls, *args, **kwargs):
        package = super(Package, cls).__new__(cls)
        package.__init__(*args, **kwargs)
        return contextlib.closing(package)

class SubPackage(Package):
    def close(self):
        pass

