# Extracted from https://stackoverflow.com/questions/12169839/which-is-the-preferred-way-to-concatenate-a-string-in-python
re.compile(
        "[A-Za-z_]"       # letter or underscore
        "[A-Za-z0-9_]*"   # letter, digit or underscore
    )

