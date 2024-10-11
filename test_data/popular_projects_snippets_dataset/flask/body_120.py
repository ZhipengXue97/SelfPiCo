# Extracted from ./data/repos/flask/src/flask/app.py
"""Returns the shell context for an interactive shell for this
        application.  This runs all the registered shell context
        processors.

        .. versionadded:: 0.11
        """
rv = {"app": self, "g": g}
for processor in self.shell_context_processors:
    rv.update(processor())
exit(rv)
