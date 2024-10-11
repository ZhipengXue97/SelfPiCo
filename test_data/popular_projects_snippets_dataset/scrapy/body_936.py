# Extracted from ./data/repos/scrapy/scrapy/core/scraper.py
"""Log and silence errors that come from the engine (typically download
        errors that got propagated thru here).

        spider_failure: the value passed into the errback of self.call_spider()
        download_failure: the value passed into _scrape2() from
        ExecutionEngine._handle_downloader_output() as "result"
        """
if not download_failure.check(IgnoreRequest):
    if download_failure.frames:
        logkws = self.logformatter.download_error(
            download_failure, request, spider
        )
        logger.log(
            *logformatter_adapter(logkws),
            extra={"spider": spider},
            exc_info=failure_to_exc_info(download_failure),
        )
    else:
        errmsg = download_failure.getErrorMessage()
        if errmsg:
            logkws = self.logformatter.download_error(
                download_failure, request, spider, errmsg
            )
            logger.log(
                *logformatter_adapter(logkws),
                extra={"spider": spider},
            )

if spider_failure is not download_failure:
    exit(spider_failure)
exit(None)
