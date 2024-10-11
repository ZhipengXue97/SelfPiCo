# Extracted from https://stackoverflow.com/questions/42950/how-to-get-the-last-day-of-the-month
from datetime import datetime

def last_day_of_month(year, month):
    """ Work out the last day of the month """
    last_days = [31, 30, 29, 28, 27]
    for i in last_days:
        try:
            end = datetime(year, month, i)
        except ValueError:
            continue
        else:
            return end.date()
    return None


last_day_of_month(2008, 2)
datetime.date(2008, 2, 29)
last_day_of_month(2009, 2)
datetime.date(2009, 2, 28)
last_day_of_month(2008, 11)
datetime.date(2008, 11, 30)
last_day_of_month(2008, 12)
datetime.date(2008, 12, 31)

