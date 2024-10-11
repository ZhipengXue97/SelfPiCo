# Extracted from https://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript
import datetime
date = datetime.datetime.today()
json = '{"mydate":new Date("%s")}' % date.ctime()

