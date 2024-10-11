# Extracted from https://stackoverflow.com/questions/13890935/does-pythons-time-time-return-the-local-or-utc-timestamp
import time, datetime

time.time()
1564494136.0434234

datetime.datetime.now()
datetime.datetime(2019, 7, 30, 16, 42, 3, 899179)
datetime.datetime.fromtimestamp(time.time())
datetime.datetime(2019, 7, 30, 16, 43, 12, 4610)

import arrow
arrow.now()
arrow.get(time.time())

