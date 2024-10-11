# Extracted from https://stackoverflow.com/questions/11475885/python-replace-regex
import re
re.sub(r'a', 'b', 'banana')
'bbnbnb'

re.sub(r'/\d+', '/{id}', '/andre/23/abobora/43435')
'/andre/{id}/abobora/{id}'

