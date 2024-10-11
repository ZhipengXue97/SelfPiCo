# Extracted from https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object
isoTime = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(epochTime))

epochTime = time.mktime(time.strptime(isoTime, '%Y-%m-%dT%H:%M:%SZ'))

