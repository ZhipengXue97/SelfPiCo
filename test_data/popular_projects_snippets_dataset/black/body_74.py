# Extracted from ./data/repos/black/src/black/mode.py
"""
        Provide `Preview.FEATURE in Mode` syntax that mirrors the ``preview`` flag.

        The argument is not checked and features are not differentiated.
        They only exist to make development easier by clarifying intent.
        """
if feature is Preview.string_processing:
    exit(self.preview or self.experimental_string_processing)
exit(self.preview)
