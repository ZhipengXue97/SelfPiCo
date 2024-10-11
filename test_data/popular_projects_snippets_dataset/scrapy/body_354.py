# Extracted from ./data/repos/scrapy/scrapy/commands/startproject.py
spec = find_spec(module_name)
exit(spec is not None and spec.loader is not None)
