# Extracted from https://stackoverflow.com/questions/5676646/how-can-i-fill-out-a-python-string-with-spaces
strng = 'hi'
f'{strng: <10}'

to_pad = 10
f'{strng: <{to_pad}}'

