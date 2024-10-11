# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
if not isinstance(failure.value, IgnoreRequest):
    referer = referer_str(request)
    logger.warning(
        "File (unknown-error): Error downloading %(medianame)s from "
        "%(request)s referred in <%(referer)s>: %(exception)s",
        {
            "medianame": self.MEDIA_NAME,
            "request": request,
            "referer": referer,
            "exception": failure.value,
        },
        extra={"spider": info.spider},
    )

raise FileException
