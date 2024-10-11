# Extracted from https://stackoverflow.com/questions/2331592/why-does-datetime-datetime-utcnow-not-contain-timezone-information
import datetime
datetime.datetime.now(datetime.timezone.utc)
datetime.datetime(2014, 7, 10, 2, 43, 55, 230107, tzinfo=datetime.timezone.utc)

