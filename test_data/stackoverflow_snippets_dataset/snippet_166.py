# Extracted from https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
len('Öl')  # German word for 'oil' with 2 characters
2
'Öl'.encode('UTF-8')  # convert str to bytes 
b'\xc3\x96l'
len('Öl'.encode('UTF-8'))  # 3 bytes encode 2 characters !
3

