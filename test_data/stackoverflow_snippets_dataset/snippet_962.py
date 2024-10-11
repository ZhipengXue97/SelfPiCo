# Extracted from https://stackoverflow.com/questions/363944/python-idiom-to-return-first-item-or-none
a = get_list()
return a[0] if a else None

return (get_list()[:1] or [None])[0]

