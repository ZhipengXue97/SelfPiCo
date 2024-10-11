# Extracted from https://stackoverflow.com/questions/181530/styling-multi-line-conditions-in-if-statements
if (
    cond1 and
    cond2
):
    print("Hello World!")

if all([
    cond1,
    cond2,
]):
    print("Hello World!")

# Check if every string in a list contains a substring:
my_list = [
    'a substring is like a string', 
    'another substring'
]

if all('substring' in item for item in my_list):
   print("Hello World!")

# or

if all(
    'substring' in item
    for item in my_list
):
    print("Hello World!")

