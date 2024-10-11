# Extracted from https://stackoverflow.com/questions/8653516/search-a-list-of-dictionaries-in-python
def find_dict_in_list(dicts, default=None, **kwargs):
    """Find first matching :obj:`dict` in :obj:`list`.

    :param list dicts: List of dictionaries.
    :param dict default: Optional. Default dictionary to return.
        Defaults to `None`.
    :param **kwargs: `key=value` pairs to match in :obj:`dict`.

    :returns: First matching :obj:`dict` from `dicts`.
    :rtype: dict

    """

    rval = default
    for d in dicts:
        is_found = False

        # Search for keys in dict.
        for k, v in kwargs.items():
            if d.get(k, None) == v:
                is_found = True

            else:
                is_found = False
                break

        if is_found:
            rval = d
            break

    return rval


if __name__ == '__main__':
    # Tests
    dicts = []
    keys = 'spam eggs shrubbery knight'.split()

    start = 0
    for _ in range(4):
        dct = {k: v for k, v in zip(keys, range(start, start+4))}
        dicts.append(dct)
        start += 4

    # Find each dict based on 'spam' key only.  
    for x in range(len(dicts)):
        spam = x*4
        assert find_dict_in_list(dicts, spam=spam) == dicts[x]

    # Find each dict based on 'spam' and 'shrubbery' keys.
    for x in range(len(dicts)):
        spam = x*4
        assert find_dict_in_list(dicts, spam=spam, shrubbery=spam+2) == dicts[x]

    # Search for one correct key, one incorrect key:
    for x in range(len(dicts)):
        spam = x*4
        assert find_dict_in_list(dicts, spam=spam, shrubbery=spam+1) is None

    # Search for non-existent dict.
    for x in range(len(dicts)):
        spam = x+100
        assert find_dict_in_list(dicts, spam=spam) is None

