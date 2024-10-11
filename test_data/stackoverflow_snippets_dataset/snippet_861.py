# Extracted from https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes
# decorators.py
def abstract(f):
    def _decorator(*_):
        raise NotImplementedError(f"Method '{f.__name__}' is abstract")
    return _decorator


# yourclass.py
class Vehicle:
    def add_energy():
       print("Energy added!")

    @abstract
    def get_make(): ...

    @abstract
    def get_model(): ...

