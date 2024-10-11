# Extracted from https://stackoverflow.com/questions/6289474/working-with-utf-8-encoding-in-python-source
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

u = 'idzie wąż wąską dróżką'
uu = u.decode('utf8')
s = uu.encode('cp1250')
print(s)

