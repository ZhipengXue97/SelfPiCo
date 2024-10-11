# Extracted from https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
from unidecode import unidecode
unidecode('kožušček')
'kozuscek'
unidecode('北亰')
'Bei Jing '
unidecode('François')
'Francois'

