# Extracted from https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()
print(html)

