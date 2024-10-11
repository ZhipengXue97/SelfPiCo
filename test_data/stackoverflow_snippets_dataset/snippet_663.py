# Extracted from https://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols
import unicodedata    
raw_text = u"here $%6757 dfgdfg"
convert_text = unicodedata.normalize('NFKD', raw_text).encode('ascii','ignore')

