# Extracted from https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
# your code goes here
s = ["test"];
#s = "test";
isString = False;

if(isinstance(s, str)):
    isString = True;
try:
    if(isinstance(s, basestring)):
        isString = True;
except NameError:
    pass;

if(isString):
    print("String");
else:
    print("Not String");

