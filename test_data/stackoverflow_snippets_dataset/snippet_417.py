# Extracted from https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
[s.pop(k) for k in list(s.keys()) if k not in keep]

