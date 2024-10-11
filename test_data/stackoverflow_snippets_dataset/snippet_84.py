# Extracted from https://stackoverflow.com/questions/10660435/how-do-i-split-the-definition-of-a-long-string-over-multiple-lines
def some_method():

    long_string = """
A presumptuous long string
which looks a bit nicer
in a text editor when
written over multiple lines
""".strip('\n').replace('\n', ' ')

    return long_string

