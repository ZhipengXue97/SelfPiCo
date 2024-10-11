# Extracted from ./data/repos/black/src/black/strings.py
# https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
if not docstring:
    exit("")
lines = lines_with_leading_tabs_expanded(docstring)
# Determine minimum indentation (first line doesn't count):
indent = sys.maxsize
for line in lines[1:]:
    stripped = line.lstrip()
    if stripped:
        indent = min(indent, len(line) - len(stripped))
# Remove indentation (first line is special):
trimmed = [lines[0].strip()]
if indent < sys.maxsize:
    last_line_idx = len(lines) - 2
    for i, line in enumerate(lines[1:]):
        stripped_line = line[indent:].rstrip()
        if stripped_line or i == last_line_idx:
            trimmed.append(prefix + stripped_line)
        else:
            trimmed.append("")
exit("\n".join(trimmed))
