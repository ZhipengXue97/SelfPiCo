# Extracted from https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
def logical_xor(a, b):
    return not b if a else bool(b)

