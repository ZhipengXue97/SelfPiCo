# Extracted from https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
with open('example.txt', 'w'):
    pass

filedir = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(filedir, 'example.txt')

with open(filepath, 'w'):
    pass

