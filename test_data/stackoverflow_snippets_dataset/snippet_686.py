# Extracted from https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
text = f'{text[:1]}Z{text[2:]}'

timeit.timeit("text = 'abcdefg'; text = text[:1] + 'Z' + text[2:]", number=1000000)
1.1691178000000093
timeit.timeit("text = 'abcdefg'; text = f'{text[:1]}Z{text[2:]}'", number =1000000)
0.9047831999999971


