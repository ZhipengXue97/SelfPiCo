# Extracted from https://stackoverflow.com/questions/4284313/how-can-i-check-the-syntax-of-python-script-without-executing-it
import sys
import glob, os

os.chdir(sys.argv[1])
for file in glob.glob("*.py"):
    source = open(file, 'r').read() + '\n'
    compile(source, file, 'exec')

