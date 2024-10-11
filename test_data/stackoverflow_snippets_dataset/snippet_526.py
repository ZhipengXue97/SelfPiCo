# Extracted from https://stackoverflow.com/questions/954834/how-do-i-use-raw-input-in-python-3
# Fix Python 2.x.
try: input = raw_input
except NameError: pass
print("Hi " + input("Say something: "))

