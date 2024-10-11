# Extracted from https://stackoverflow.com/questions/12453580/how-to-concatenate-join-items-in-a-list-to-a-single-string
list_abc = ['aaa', 'bbb', 'ccc']

string = ''.join(list_abc)
print(string)
aaabbbccc

string = ','.join(list_abc)
print(string)
aaa,bbb,ccc

string = '-'.join(list_abc)
print(string)
aaa-bbb-ccc

string = '\n'.join(list_abc)
print(string)
aaa
bbb
ccc

