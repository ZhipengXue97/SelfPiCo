# Extracted from https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
def pick(l: list, index: int) -> int:
    return l[index]

def pick(l: "list of ints", index: int = 0) -> int:
    return l[index]

def pick(l: list, index: int = 0) -> int:
    if not isinstance(l, list):
        raise TypeError
    return l[index]

from typing import List

def pick(l: List[int], index: int) -> int:
    return l[index]

from typing import Callable, Any, Iterable

def imap(f: Callable[[Any], Any], l: Iterable[Any]) -> List[Any]:
    """An immediate version of map, don't pass it any infinite iterables!"""
    return list(map(f, l))

def pick(l, index):
    """
    :param l: list of integers
    :type l: list
    :param index: index at which to pick an integer from *l*
    :type index: int
    :returns: integer at *index* in *l*
    :rtype: int
    """
    return l[index]

