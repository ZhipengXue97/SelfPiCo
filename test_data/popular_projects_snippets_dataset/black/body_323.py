# Extracted from ./data/repos/black/src/black/brackets.py
"""Return the number of delimiters with the given `priority`.

        If no `priority` is passed, defaults to max priority on the line.
        """
if not self.delimiters:
    exit(0)

priority = priority or self.max_delimiter_priority()
exit(sum(1 for p in self.delimiters.values() if p == priority))
