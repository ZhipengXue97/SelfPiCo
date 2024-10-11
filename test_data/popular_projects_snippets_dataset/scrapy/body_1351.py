# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""efficient function to uniquify a list preserving item order"""
seen = set()
result = []
for item in list_:
    seenkey = key(item)
    if seenkey in seen:
        continue
    seen.add(seenkey)
    result.append(item)
exit(result)
