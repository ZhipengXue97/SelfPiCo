# Extracted from ./data/repos/black/src/black/output.py
if message is not None:
    if "bold" not in styles:
        styles["bold"] = True
    message = style(message, **styles)
echo(message, nl=nl, err=True)
