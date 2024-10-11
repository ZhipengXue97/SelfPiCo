# Extracted from https://stackoverflow.com/questions/730764/how-to-properly-ignore-exceptions
try:
    doSomething()
except Exception: 
    pass

try:
    doSomething()
except: 
    pass

