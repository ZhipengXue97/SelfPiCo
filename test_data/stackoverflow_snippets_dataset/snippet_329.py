# Extracted from https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-handling-file-conte
# -*- coding: utf-8 -*-
print(bytes('ò'))

print(bytes('ò', 'iso_8859_1')) # prints: b'\xf2'
print(bytes('ò', 'utf-8')) # prints: b'\xc3\xb2'

