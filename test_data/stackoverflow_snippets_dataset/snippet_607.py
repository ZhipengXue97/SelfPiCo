# Extracted from https://stackoverflow.com/questions/9475241/split-string-every-nth-character
s = '1234567890'
print([s[idx:idx+2] for idx in range(len(s)) if idx % 2 == 0])

['12', '34', '56', '78', '90']

