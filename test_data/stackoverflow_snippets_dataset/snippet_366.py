# Extracted from https://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
#to import from one level above:
cwd = os.getcwd()
os.chdir("..")
below_path =  os.getcwd()
sys.path.append(below_path)
os.chdir(cwd)

