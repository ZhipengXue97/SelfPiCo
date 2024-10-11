# Extracted from https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
csv_data = pd.read_csv(csvpath,encoding='iso-8859-1')
print(print(soup.encode('iso-8859-1')))

