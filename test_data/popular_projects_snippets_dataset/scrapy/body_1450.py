# Extracted from ./data/repos/scrapy/scrapy/pipelines/images.py
if response_body is None:
    warnings.warn(
        f"{self.__class__.__name__}.convert_image() method called in a deprecated way, "
        "method called without response_body argument.",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )

if image.format in ("PNG", "WEBP") and image.mode == "RGBA":
    background = self._Image.new("RGBA", image.size, (255, 255, 255))
    background.paste(image, image)
    image = background.convert("RGB")
elif image.mode == "P":
    image = image.convert("RGBA")
    background = self._Image.new("RGBA", image.size, (255, 255, 255))
    background.paste(image, image)
    image = background.convert("RGB")
elif image.mode != "RGB":
    image = image.convert("RGB")

if size:
    image = image.copy()
    try:
        # Image.Resampling.LANCZOS was added in Pillow 9.1.0
        # remove this try except block,
        # when updating the minimum requirements for Pillow.
        resampling_filter = self._Image.Resampling.LANCZOS
    except AttributeError:
        resampling_filter = self._Image.ANTIALIAS
    image.thumbnail(size, resampling_filter)
elif response_body is not None and image.format == "JPEG":
    exit((image, response_body))

buf = BytesIO()
image.save(buf, "JPEG")
exit((image, buf))
