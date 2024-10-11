# Extracted from ./data/repos/scrapy/scrapy/extensions/logstats.py
items = self.stats.get_value("item_scraped_count", 0)
pages = self.stats.get_value("response_received_count", 0)
irate = (items - self.itemsprev) * self.multiplier
prate = (pages - self.pagesprev) * self.multiplier
self.pagesprev, self.itemsprev = pages, items

msg = (
    "Crawled %(pages)d pages (at %(pagerate)d pages/min), "
    "scraped %(items)d items (at %(itemrate)d items/min)"
)
log_args = {
    "pages": pages,
    "pagerate": prate,
    "items": items,
    "itemrate": irate,
}
logger.info(msg, log_args, extra={"spider": spider})
