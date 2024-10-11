# Extracted from https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
with open('data.txt', 'r') as file:
    data = file.read().replace('\n', '')

with open('data.txt', 'r') as file:
    data = file.read().rstrip()

