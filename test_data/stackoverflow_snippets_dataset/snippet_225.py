# Extracted from https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
timestamp ="124542124"
value = datetime.datetime.fromtimestamp(timestamp)
exct_time = value.strftime('%d %B %Y %H:%M:%S')

