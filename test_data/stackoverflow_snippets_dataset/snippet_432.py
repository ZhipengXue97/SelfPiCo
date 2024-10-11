# Extracted from https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python
import requests
requests.get('http://youraddress.com', params=evt.fields)

params=[('name1','value11'), ('name1','value12'), ('name2','value21'), ...]

