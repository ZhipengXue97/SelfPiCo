# Extracted from https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time
import datetime

now = datetime.datetime.now()
print(now)

import datetime

now = datetime.datetime.now()
print(now.strftime("%Y-%b-%d, %A %I:%M:%S"))

