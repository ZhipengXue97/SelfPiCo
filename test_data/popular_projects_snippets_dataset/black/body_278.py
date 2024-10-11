# Extracted from ./data/repos/black/src/black/output.py
if message is not None:
    if "fg" not in styles:
        styles["fg"] = "red"
    message = style(message, **styles)
echo(message, nl=nl, err=True)
