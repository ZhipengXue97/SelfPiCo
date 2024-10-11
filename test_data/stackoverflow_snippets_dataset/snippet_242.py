# Extracted from https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
import glob, os
os.chdir("H:\\wallpaper")# use whatever directory you want

#double\\ no single \

for file in glob.glob("**/*.txt", recursive = True):
    print(file)

