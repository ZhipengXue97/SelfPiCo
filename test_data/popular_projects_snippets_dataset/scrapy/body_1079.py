# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
plugins = [load_object(plugin) for plugin in plugins]
exit(plugins)
