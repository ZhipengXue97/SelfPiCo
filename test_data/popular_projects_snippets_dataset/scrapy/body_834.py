# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
"""Return a deferred for the HTTP download"""
agent = ScrapyAgent(
    contextFactory=self._contextFactory,
    pool=self._pool,
    maxsize=getattr(spider, "download_maxsize", self._default_maxsize),
    warnsize=getattr(spider, "download_warnsize", self._default_warnsize),
    fail_on_dataloss=self._fail_on_dataloss,
    crawler=self._crawler,
)
exit(agent.download_request(request))
