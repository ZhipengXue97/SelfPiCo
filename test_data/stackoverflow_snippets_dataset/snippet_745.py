# Extracted from https://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-is-a-string
# NOTE: fields is an object that COULD be any number of things, including:
# - a single string-like object
# - a string-like object that needs to be converted to a sequence of 
# string-like objects at some separator, sep
# - a sequence of string-like objects
def getfields(*fields, sep=' ', validator=lambda f: True):
    '''Take a field sequence definition and yield from a validated
     field sequence. Accepts a string, a string with separators, 
     or a sequence of strings'''
    if fields:
        try:
            # single unpack in the case of a single argument
            fieldseq, = fields
            try:
                # convert to string sequence if string
                fieldseq = fieldseq.split(sep)
            except AttributeError:
                # not a string; assume other iterable
                pass
        except ValueError:
            # not a single argument and not a string
            fieldseq = fields
        invalid_fields = [field for field in fieldseq if not validator(field)]
        if invalid_fields:
            raise ValueError('One or more field names is invalid:\n'
                             '{!r}'.format(invalid_fields))
    else:
        raise ValueError('No fields were provided')
    try:
        yield from fieldseq
    except TypeError as e:
        raise ValueError('Single field argument must be a string'
                         'or an interable') from e

from . import getfields

def test_getfields_novalidation():
    result = ['a', 'b']
    assert list(getfields('a b')) == result
    assert list(getfields('a,b', sep=',')) == result
    assert list(getfields('a', 'b')) == result
    assert list(getfields(['a', 'b'])) == result

