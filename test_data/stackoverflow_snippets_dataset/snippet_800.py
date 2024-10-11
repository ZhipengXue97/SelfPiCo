# Extracted from https://stackoverflow.com/questions/2803852/python-date-string-to-date-object
import arrow
import datetime

a = arrow.get('24052010', 'DMYYYY').date()
print(isinstance(a, datetime.date)) # True

