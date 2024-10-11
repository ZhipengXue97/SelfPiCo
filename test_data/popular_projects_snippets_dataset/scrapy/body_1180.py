# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
"""The policy functions from asyncio often behave unexpectedly,
    so we restrict their use to the absolutely essential case.
    This should only be used to install the reactor.
    """
_get_asyncio_event_loop_policy()
