# Extracted from https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
from datetime import datetime
import pytz

tz = pytz.timezone('US/Pacific')
datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
# '2021-09-02 10:21:41'

