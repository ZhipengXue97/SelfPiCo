# Extracted from https://stackoverflow.com/questions/2835559/why-cant-python-parse-this-json-data
{
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": [{
        "id": "valore"
    }],
    "om_points": "value",
    "parameters": [{
        "id": "valore"
    }]
}

import json
from pprint import pprint
with open('data.json') as data_file:
    data_item = json.load(data_file)
pprint(data_item)

{'maps': [{'id': 'blabla', 'iscategorical': '0'},
          {'id': 'blabla', 'iscategorical': '0'}],
 'masks': [{'id': 'valore'}],
 'om_points': 'value',
 'parameters': [{'id': 'valore'}]}

valore

