# Extracted from https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
import glob

for filepath in glob.iglob('my_dir/*.asm'):
    print(filepath)

glob.glob('**/*.txt', recursive=True) # => ['2.txt', 'sub/3.txt']

