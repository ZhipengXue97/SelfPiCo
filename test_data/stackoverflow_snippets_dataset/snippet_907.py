# Extracted from https://stackoverflow.com/questions/8949252/why-do-i-get-attributeerror-nonetype-object-has-no-attribute-something
def return_something(someint):
 if  someint > 5:
    return someint

y = return_something(2)
y.real()

