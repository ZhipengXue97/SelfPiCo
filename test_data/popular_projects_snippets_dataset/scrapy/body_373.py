# Extracted from ./data/repos/scrapy/scrapy/commands/shell.py
url = args[0] if args else None
if url:
    # first argument may be a local file
    url = guess_scheme(url)

spider_loader = self.crawler_process.spider_loader

spidercls = DefaultSpider
if opts.spider:
    spidercls = spider_loader.load(opts.spider)
elif url:
    spidercls = spidercls_for_request(
        spider_loader, Request(url), spidercls, log_multiple=True
    )

# The crawler is created this way since the Shell manually handles the
# crawling engine, so the set up in the crawl method won't work
crawler = self.crawler_process._create_crawler(spidercls)
# The Shell class needs a persistent engine in the crawler
crawler.engine = crawler._create_engine()
crawler.engine.start()

self._start_crawler_thread()

shell = Shell(crawler, update_vars=self.update_vars, code=opts.code)
shell.start(url=url, redirect=not opts.no_redirect)
