# Extracted from ./data/repos/scrapy/scrapy/utils/reactor.py
warn(
    "Call to deprecated function "
    "scrapy.utils.reactor.get_asyncio_event_loop_policy().\n"
    "\n"
    "Please use get_event_loop, new_event_loop and set_event_loop"
    " from asyncio instead, as the corresponding policy methods may lead"
    " to unexpected behaviour.\n"
    "This function is replaced by set_asyncio_event_loop_policy and"
    " is meant to be used only when the reactor is being installed.",
    category=ScrapyDeprecationWarning,
    stacklevel=2,
)
exit(_get_asyncio_event_loop_policy())
