# Extracted from https://stackoverflow.com/questions/37031928/type-annotations-for-args-and-kwargs
def foo(param, *args, **kwargs):
    # type: (bool, *str, **int) -> None
    pass

def foo(param: bool, *args: str, **kwargs: int) -> None:
    pass

