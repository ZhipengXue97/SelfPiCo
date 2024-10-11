# Extracted from https://stackoverflow.com/questions/4690600/python-exception-message-capturing
arr = ["a", "b", "c"]

try:
    print(arr[5])
except IndexError as ex:
    print(repr(ex)) # IndexError: list index out of range
    print(str(ex)) # list index out of range

