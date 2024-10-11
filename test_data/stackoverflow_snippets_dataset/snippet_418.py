# Extracted from https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
a='Beautiful, is; better*than\nugly'
import re
re.split('; |, |\*|\n',a)
['Beautiful', 'is', 'better', 'than', 'ugly']

b='1999-05-03 10:37:00'
re.split('- :', b)
['1999-05-03 10:37:00']

re.split('[- :]', b)
['1999', '05', '03', '10', '37', '00']

