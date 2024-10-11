# Extracted from https://stackoverflow.com/questions/1549641/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string
s = 'the brown fox'
lst = [word[0].upper() + word[1:] for word in s.split()]
s = " ".join(lst)

s = 'the brown fox'
s = ' '.join(word[0].upper() + word[1:] for word in s.split())

import re
s = 'the brown fox'

def repl_func(m):
    """process regular expression match groups for word upper-casing problem"""
    return m.group(1) + m.group(2).upper()

s = re.sub("(^|\s)(\S)", repl_func, s)


re.sub("(^|\s)(\S)", repl_func, s)
"They're Bill's Friends From The UK"

