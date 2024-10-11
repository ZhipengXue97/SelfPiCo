# Extracted from ./data/repos/scrapy/scrapy/crawler.py
"""Get SpiderLoader instance from settings"""
cls_path = settings.get("SPIDER_LOADER_CLASS")
loader_cls = load_object(cls_path)
excs = (
    (DoesNotImplement, MultipleInvalid) if MultipleInvalid else DoesNotImplement
)
try:
    verifyClass(ISpiderLoader, loader_cls)
except excs:
    warnings.warn(
        "SPIDER_LOADER_CLASS (previously named SPIDER_MANAGER_CLASS) does "
        "not fully implement scrapy.interfaces.ISpiderLoader interface. "
        "Please add all missing methods to avoid unexpected runtime errors.",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )
exit(loader_cls.from_settings(settings.frozencopy()))
