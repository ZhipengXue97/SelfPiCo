# Extracted from https://stackoverflow.com/questions/18337407/saving-utf-8-texts-with-json-dumps-as-utf-8-not-as-a-u-escape-sequence
def jsonWrite(p, pyobj, ensure_ascii=False, encoding=SYSTEM_ENCODING, **kwargs):
    with codecs.open(p, 'wb', 'utf_8') as fileobj:
        json.dump(pyobj, fileobj, ensure_ascii=ensure_ascii,encoding=encoding, **kwargs)

locale.setlocale(locale.LC_ALL, '')
SYSTEM_ENCODING = locale.getlocale()[1]

