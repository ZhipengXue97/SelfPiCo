# Extracted from ./data/repos/scrapy/scrapy/utils/signal.py
"""Like send_catch_log but supports returning deferreds on signal handlers.
    Returns a deferred that gets fired once all signal handlers deferreds were
    fired.
    """

def logerror(failure, recv):
    if dont_log is None or not isinstance(failure.value, dont_log):
        logger.error(
            "Error caught on signal handler: %(receiver)s",
            {"receiver": recv},
            exc_info=failure_to_exc_info(failure),
            extra={"spider": spider},
        )
    exit(failure)

dont_log = named.pop("dont_log", None)
spider = named.get("spider", None)
dfds = []
for receiver in liveReceivers(getAllReceivers(sender, signal)):
    d = maybeDeferred_coro(
        robustApply, receiver, signal=signal, sender=sender, *arguments, **named
    )
    d.addErrback(logerror, receiver)
    d.addBoth(lambda result: (receiver, result))
    dfds.append(d)
d = DeferredList(dfds)
d.addCallback(lambda out: [x[1] for x in out])
exit(d)
