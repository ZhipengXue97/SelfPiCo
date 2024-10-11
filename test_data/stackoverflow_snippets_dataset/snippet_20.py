# Extracted from https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
def bin2str(text, encoding = 'utf-8'):
    """Converts a binary to Unicode string by removing all non Unicode char
    text: binary string to work on
    encoding: output encoding *utf-8"""

    return text.decode(encoding, 'ignore')

