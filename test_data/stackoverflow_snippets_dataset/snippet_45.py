# Extracted from https://stackoverflow.com/questions/466345/convert-string-jun-1-2005-133pm-into-datetime
from datetime import date
date_from_yyyy_mm_dd = lambda δ : date(*[int(_) for _ in δ.split('-')])
date_object = date_from_yyyy_mm_dd('2021-02-15')

