# Extracted from ./data/repos/scrapy/scrapy/spiderloader.py
self.spider_modules = settings.getlist("SPIDER_MODULES")
self.warn_only = settings.getbool("SPIDER_LOADER_WARN_ONLY")
self._spiders: Dict[str, Type[Spider]] = {}
self._found: DefaultDict[str, List[Tuple[str, str]]] = defaultdict(list)
self._load_all_spiders()
