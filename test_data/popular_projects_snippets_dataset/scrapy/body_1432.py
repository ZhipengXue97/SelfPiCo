# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
store_uri = _to_string(store_uri)
if not store_uri:
    raise NotConfigured

if isinstance(settings, dict) or settings is None:
    settings = Settings(settings)
cls_name = "FilesPipeline"
self.store = self._get_store(store_uri)
resolve = functools.partial(
    self._key_for_pipe, base_class_name=cls_name, settings=settings
)
self.expires = settings.getint(resolve("FILES_EXPIRES"), self.EXPIRES)
if not hasattr(self, "FILES_URLS_FIELD"):
    self.FILES_URLS_FIELD = self.DEFAULT_FILES_URLS_FIELD
if not hasattr(self, "FILES_RESULT_FIELD"):
    self.FILES_RESULT_FIELD = self.DEFAULT_FILES_RESULT_FIELD
self.files_urls_field = settings.get(
    resolve("FILES_URLS_FIELD"), self.FILES_URLS_FIELD
)
self.files_result_field = settings.get(
    resolve("FILES_RESULT_FIELD"), self.FILES_RESULT_FIELD
)

super().__init__(download_func=download_func, settings=settings)
