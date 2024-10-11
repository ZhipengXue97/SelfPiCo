# Extracted from https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python
a = 5
b = 6

assert a == b

AssertionError

def get_dict_key(d, k):
    try:
        assert k in d
        return d[k]
    except Exception:
        print("Key must be in dict.")

