# Extracted from https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal
'{type_names} [a-z]{2}'.format(type_names='triangle|square')

'%(type_names)s [a-z]{2}' % {'type_names': 'triangle|square'}

