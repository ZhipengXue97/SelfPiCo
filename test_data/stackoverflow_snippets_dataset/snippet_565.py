# Extracted from https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
from datetime import datetime
from time import strftime


# Get the current time in the format: 2021-03-20T16:51:23.644+01:00
def rfc3339_time_ms():
        datetime_now = datetime.utcnow()
        # Remove the microseconds
        datetime_now_ms = datetime_now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
        # Add the timezone as "+/-HHMM", and the colon in "+/-HH:MM"
        datetime_now_ms_tz = datetime_now_ms + strftime("%z")
        rfc3339_ms_now = datetime_now_ms_tz[:-2] + ":" + datetime_now_ms_tz[-2:]
        # print(f"Current time in ms in RFC-3339 format: {rfc3339_ms_now}")
        return rfc3339_ms_now

