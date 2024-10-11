# Extracted from ./data/repos/black/src/black/concurrency.py
"""Cancel all pending tasks on `loop`, wait for them, and close the loop."""
try:
    # This part is borrowed from asyncio/runners.py in Python 3.7b2.
    to_cancel = [task for task in asyncio.all_tasks(loop) if not task.done()]
    if not to_cancel:
        exit()

    for task in to_cancel:
        task.cancel()
    loop.run_until_complete(asyncio.gather(*to_cancel, return_exceptions=True))
finally:
    # `concurrent.futures.Future` objects cannot be cancelled once they
    # are already running. There might be some when the `shutdown()` happened.
    # Silence their logger's spew about the event loop being closed.
    cf_logger = logging.getLogger("concurrent.futures")
    cf_logger.setLevel(logging.CRITICAL)
    loop.close()
