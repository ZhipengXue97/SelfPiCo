# Extracted from ./data/repos/scrapy/scrapy/loader/__init__.py
if selector is None and response is not None:
    try:
        selector = self.default_selector_class(response)
    except AttributeError:
        selector = None
context.update(response=response)
super().__init__(item=item, selector=selector, parent=parent, **context)
