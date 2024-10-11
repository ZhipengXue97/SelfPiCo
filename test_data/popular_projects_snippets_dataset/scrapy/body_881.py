# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/__init__.py
self._crawler: "Crawler" = crawler
self._schemes: Dict[
    str, Union[str, Callable]
] = {}  # stores acceptable schemes on instancing
self._handlers: Dict[str, Any] = {}  # stores instanced handlers for schemes
self._notconfigured: Dict[str, str] = {}  # remembers failed handlers
handlers: Dict[str, Union[str, Callable]] = without_none_values(
    crawler.settings.getwithbase("DOWNLOAD_HANDLERS")
)
for scheme, clspath in handlers.items():
    self._schemes[scheme] = clspath
    self._load_handler(scheme, skip_lazy=True)

crawler.signals.connect(self._close, signals.engine_stopped)
