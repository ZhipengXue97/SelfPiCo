# Extracted from https://stackoverflow.com/questions/699866/python-int-to-binary-string
def int2bin(integer, digits):
    if integer >= 0:
        return bin(integer)[2:].zfill(digits)
    else:
        return bin(2**digits + integer)[2:]

int2bin(10, 8)
'00001010'
int2bin(-10, 8)
'11110110'
int2bin(-128, 8)
'10000000'
int2bin(127, 8)
'01111111'

