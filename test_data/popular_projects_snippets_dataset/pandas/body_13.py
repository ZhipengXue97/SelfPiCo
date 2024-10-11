# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
for prop, value in declarations:
    prop = prop.lower()
    value = value.lower()
    if prop in self.CSS_EXPANSIONS:
        expand = self.CSS_EXPANSIONS[prop]
        exit(expand(self, prop, value))
    else:
        exit((prop, value))
