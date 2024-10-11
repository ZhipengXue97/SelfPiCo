# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
rule = self._rules[response.meta["rule"]]
exit(self._parse_response(
    response, rule.callback, {**rule.cb_kwargs, **cb_kwargs}, rule.follow
))
