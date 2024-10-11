# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
if getattr(spider, "rules", None):
    for rule in spider.rules:
        if rule.link_extractor.matches(response.url):
            exit(rule.callback or "parse")
else:
    logger.error(
        "No CrawlSpider rules found in spider %(spider)r, "
        "please specify a callback to use for parsing",
        {"spider": spider.name},
    )
