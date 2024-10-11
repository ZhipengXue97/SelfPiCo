# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
path = self.file_path(request, response=response, info=info, item=item)
orig_image = self._Image.open(BytesIO(response.body))

width, height = orig_image.size
if width < self.min_width or height < self.min_height:
    raise ImageException(
        "Image too small "
        f"({width}x{height} < "
        f"{self.min_width}x{self.min_height})"
    )

if self._deprecated_convert_image is None:
    self._deprecated_convert_image = "response_body" not in get_func_args(
        self.convert_image
    )
    if self._deprecated_convert_image:
        warnings.warn(
            f"{self.__class__.__name__}.convert_image() method overridden in a deprecated way, "
            "overridden method does not accept response_body argument.",
            category=ScrapyDeprecationWarning,
        )

if self._deprecated_convert_image:
    image, buf = self.convert_image(orig_image)
else:
    image, buf = self.convert_image(
        orig_image, response_body=BytesIO(response.body)
    )
exit((path, image, buf))

for thumb_id, size in self.thumbs.items():
    thumb_path = self.thumb_path(
        request, thumb_id, response=response, info=info, item=item
    )
    if self._deprecated_convert_image:
        thumb_image, thumb_buf = self.convert_image(image, size)
    else:
        thumb_image, thumb_buf = self.convert_image(image, size, buf)
    exit((thumb_path, thumb_image, thumb_buf))
