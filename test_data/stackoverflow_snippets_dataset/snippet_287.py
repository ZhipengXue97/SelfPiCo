# Extracted from https://stackoverflow.com/questions/1937622/convert-date-to-datetime-in-python
args = d.timetuple()[:6]
datetime.datetime(*args)

