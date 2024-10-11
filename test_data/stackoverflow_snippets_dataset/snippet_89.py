# Extracted from https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
import pprint
import json 
from urllib.request import urlopen # (Only used to get this example)

# Getting a JSON example for this example 
r = urlopen("https://mdn.github.io/fetch-examples/fetch-json/products.json")
text = r.read() 

# To print it
pprint.pprint(json.loads(text))

