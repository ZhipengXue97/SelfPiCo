# Extracted from https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
def sum(nums):
    """Expect an iterable of integers and return the sum."""
    result = 0
    for n in nums:
        result += n
    return result

def sum(nums):
    """Try to catch exceptions?"""
    try:
        result = 0
        for n in nums:
            result += n
        return result
    except TypeError as e:
        print(e)

def sum(nums):
    """
    Try to catch all of our exceptions only.
    Re-raise them with more specific details.
    """
    result = 0

    try:
        iter(nums)
    except TypeError as e:
        raise TypeError("nums must be iterable")

    for n in nums:
        try:
            result += int(n)
        except TypeError as e:
            raise TypeError("stopped mid iteration since a non-integer was found")

    return result

from typing import Iterable

def sum(nums: Iterable[int]) -> int:
    result = 0
    for n in nums:
        result += n
    return result

