# Extracted from https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
','.join([str(word) for word in wordList])

wordList = ['USD', 'EUR', 'JPY', 'NZD', 'CHF', 'CAD']
stringText = ''

for word in wordList:
    stringText += word + ','

stringText = stringText[:-2]   # get rid of last comma
print(stringText)

