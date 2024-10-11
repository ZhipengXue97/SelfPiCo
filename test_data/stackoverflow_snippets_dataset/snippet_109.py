# Extracted from https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
import json
with open('data.json', 'w') as f:
    json.dump(data, f)

import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

