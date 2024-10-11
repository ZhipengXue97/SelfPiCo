# Extracted from https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d1 - d0
print(delta.days)

