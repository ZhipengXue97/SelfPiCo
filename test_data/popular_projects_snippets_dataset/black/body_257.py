# Extracted from ./data/repos/black/src/black/concurrency.py
"""asyncio signal handler that cancels all `tasks` and reports to stderr."""
err("Aborted!")
for task in tasks:
    task.cancel()
