# Extracted from https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
content ="Prefix_helloworld_Suffix_stuff_Prefix_42_Suffix_andsoon"
strings = []
for c in content.split('Prefix_'):
    spos = c.find('_Suffix')
    if spos!=-1:
        strings.append( c[:spos])
print( strings )

strings = [ c[:c.find('_Suffix')] for c in content.split('Prefix_') if c.find('_Suffix')!=-1 ]

