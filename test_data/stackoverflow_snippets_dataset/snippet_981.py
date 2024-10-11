# Extracted from https://stackoverflow.com/questions/79797/how-to-convert-local-time-string-to-utc
from time import strftime, gmtime, localtime
strftime('%H:%M:%S', gmtime()) #UTC time
strftime('%H:%M:%S', localtime()) # localtime

