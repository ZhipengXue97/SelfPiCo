# Extracted from https://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python
import re
s = "many   fancy word \nhello    \thi"
re.findall(r'\S+', s)
['many', 'fancy', 'word', 'hello', 'hi']

