# Extracted from https://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist
import os, platform
os.chdir('c:\\Users\\MS\\Desktop')

try :
    file = open("Learn Python.txt","a")
    print('this file is exist')
except:
    print('this file is not exist')
file.write('\n''Hello Ashok')

fhead = open('Learn Python.txt')

for line in fhead:

    words = line.split()
print(words)

