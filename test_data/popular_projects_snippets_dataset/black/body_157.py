# Extracted from ./data/repos/black/src/black/lines.py
"""Like `reversed(enumerate(sequence))` if that were possible."""
index = len(sequence) - 1
for element in reversed(sequence):
    exit((index, element))
    index -= 1
