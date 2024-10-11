# Extracted from ./data/repos/black/src/black/output.py
"""Dump `output` to a temporary file. Return path to the file."""
with tempfile.NamedTemporaryFile(
    mode="w", prefix="blk_", suffix=".log", delete=False, encoding="utf8"
) as f:
    for lines in output:
        f.write(lines)
        if ensure_final_newline and lines and lines[-1] != "\n":
            f.write("\n")
exit(f.name)
