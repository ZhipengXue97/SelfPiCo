# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
try:
    from PIL import Image

    self._Image = Image
except ImportError:
    raise NotConfigured(
        "ImagesPipeline requires installing Pillow 4.0.0 or later"
    )

super().__init__(store_uri, settings=settings, download_func=download_func)

if isinstance(settings, dict) or settings is None:
    settings = Settings(settings)

resolve = functools.partial(
    self._key_for_pipe,
    base_class_name="ImagesPipeline",
    settings=settings,
)
self.expires = settings.getint(resolve("IMAGES_EXPIRES"), self.EXPIRES)

if not hasattr(self, "IMAGES_RESULT_FIELD"):
    self.IMAGES_RESULT_FIELD = self.DEFAULT_IMAGES_RESULT_FIELD
if not hasattr(self, "IMAGES_URLS_FIELD"):
    self.IMAGES_URLS_FIELD = self.DEFAULT_IMAGES_URLS_FIELD

self.images_urls_field = settings.get(
    resolve("IMAGES_URLS_FIELD"), self.IMAGES_URLS_FIELD
)
self.images_result_field = settings.get(
    resolve("IMAGES_RESULT_FIELD"), self.IMAGES_RESULT_FIELD
)
self.min_width = settings.getint(resolve("IMAGES_MIN_WIDTH"), self.MIN_WIDTH)
self.min_height = settings.getint(resolve("IMAGES_MIN_HEIGHT"), self.MIN_HEIGHT)
self.thumbs = settings.get(resolve("IMAGES_THUMBS"), self.THUMBS)

self._deprecated_convert_image = None
