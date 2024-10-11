# Extracted from https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
file = open(filename)
text = file.read()

file = open(filename, errors='replace')

file = open(filename, errors='ignore')

file = open(filename, encoding='cp437')

