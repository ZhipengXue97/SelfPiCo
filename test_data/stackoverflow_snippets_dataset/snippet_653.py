# Extracted from https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
import datetime
datetime.datetime.now().replace(microsecond=0).isoformat()
# Returns: '2017-01-23T14:58:07'

datetime.datetime.now().replace(microsecond=0).isoformat(' ')
# Returns: '2017-01-23 15:05:27'

