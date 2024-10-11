# Extracted from https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
def find_first_digit(s, non=False):
    for i, x in enumerate(s):
        if x.isdigit() ^ non:
            return i
    return -1

def split_digits(s, case=False):
    non = True
    while s:
        i = find_first_digit(s, non)
        if i == 0:
            non = not non
        elif i == -1:
            yield int(s) if s.isdigit() else s if case else s.lower()
            s = ''
        else:
            x, s = s[:i], s[i:]
            yield int(x) if x.isdigit() else x if case else x.lower()

def natural_key(s, *args, **kwargs):
    return tuple(split_digits(s, *args, **kwargs))

# Note that the key has lower case letters
natural_key('asl;dkfDFKJ:sdlkfjdf809lkasdjfa_543_hh')

('asl;dkfdfkj:sdlkfjdf', 809, 'lkasdjfa_', 543, '_hh')

natural_key('asl;dkfDFKJ:sdlkfjdf809lkasdjfa_543_hh', True)

('asl;dkfDFKJ:sdlkfjdf', 809, 'lkasdjfa_', 543, '_hh')

sorted(
    ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13'],
    key=natural_key
)

['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']

sorted(
    ['f_1', 'e_1', 'a_2', 'g_0', 'd_0_12:2', 'd_0_1_:2'],
    key=natural_key
)

['a_2', 'd_0_1_:2', 'd_0_12:2', 'e_1', 'f_1', 'g_0']

def int_maybe(x):
    return int(x) if str(x).isdigit() else x

def split_digits_re(s, case=False):
    parts = re.findall('\d+|\D+', s)
    if not case:
        return map(int_maybe, (x.lower() for x in parts))
    else:
        return map(int_maybe, parts)
    
def natural_key_re(s, *args, **kwargs):
    return tuple(split_digits_re(s, *args, **kwargs))

