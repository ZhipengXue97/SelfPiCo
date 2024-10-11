# Extracted from https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
import pycron
import time

while True:
    if pycron.is_now('0 2 * * 0'):   # True Every Sunday at 02:00
        print('running backup')
        time.sleep(60)               # The process should take at least 60 sec
                                     # to avoid running twice in one minute
    else:
        time.sleep(15)               # Check again in 15 seconds

