# Extracted from ./data/repos/black/src/black/output.py
"""Inject the ANSI color codes to the diff."""
lines = contents.split("\n")
for i, line in enumerate(lines):
    if line.startswith("+++") or line.startswith("---"):
        line = "\033[1m" + line + "\033[0m"  # bold, reset
    elif line.startswith("@@"):
        line = "\033[36m" + line + "\033[0m"  # cyan, reset
    elif line.startswith("+"):
        line = "\033[32m" + line + "\033[0m"  # green, reset
    elif line.startswith("-"):
        line = "\033[31m" + line + "\033[0m"  # red, reset
    lines[i] = line
exit("\n".join(lines))
