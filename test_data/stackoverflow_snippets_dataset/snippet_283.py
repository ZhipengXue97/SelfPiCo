# Extracted from https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function
def a():pass
type(a) #<class 'function'>
str(type(a))=="<class 'function'>" #True

b = lambda x:x*2
str(type(b))=="<class 'function'>" #True

