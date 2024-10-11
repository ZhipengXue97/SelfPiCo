# Extracted from https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python
from datetime import datetime
then = datetime(2012, 3, 5, 23, 8, 15)        # Random date in the past
now  = datetime.now()                         # Now
duration = now - then                         # For build-in functions
duration_in_s = duration.total_seconds()      # Total number of seconds between dates

years = divmod(duration_in_s, 31536000)[0]    # Seconds in a year=365*24*60*60 = 31536000.

days  = duration.days                         # Build-in datetime function
days  = divmod(duration_in_s, 86400)[0]       # Seconds in a day = 86400

hours = divmod(duration_in_s, 3600)[0]        # Seconds in an hour = 3600

minutes = divmod(duration_in_s, 60)[0]        # Seconds in a minute = 60

seconds = duration.seconds                    # Build-in datetime function
seconds = duration_in_s

microseconds = duration.microseconds          # Build-in datetime function

days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
minutes = divmod(hours[1], 60)                # Use remainder of hours to calc minutes
seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc seconds
print("Time between dates: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))

print(now - then)

from datetime import datetime

def getDuration(then, now = datetime.now(), interval = "default"):

    # Returns a duration as specified by variable interval
    # Functions, except totalDuration, returns [quotient, remainder]

    duration = now - then # For build-in functions
    duration_in_s = duration.total_seconds() 
    
    def years():
      return divmod(duration_in_s, 31536000) # Seconds in a year=31536000.

    def days(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
      if seconds != None:
        return divmod(seconds, 1)   
      return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "Time between dates: {} years, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(d[0]), int(h[0]), int(m[0]), int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    }[interval]

# Example usage
then = datetime(2012, 3, 5, 23, 8, 15)
now = datetime.now()

print(getDuration(then)) # E.g. Time between dates: 7 years, 208 days, 21 hours, 19 minutes and 15 seconds
print(getDuration(then, now, 'years'))      # Prints duration in years
print(getDuration(then, now, 'days'))       #                    days
print(getDuration(then, now, 'hours'))      #                    hours
print(getDuration(then, now, 'minutes'))    #                    minutes
print(getDuration(then, now, 'seconds'))    #                    seconds

start = datetime(2020,12,31,22,0,0,500)
end = datetime(2020,12,31,23,0,0,700)
delta = end - start
delta.microseconds
RESULT: 200
EXPECTED: 3600000200

start = datetime(2020,12,30,22,0,0)
end = datetime(2020,12,31,23,0,0)
delta = end - start
delta.seconds
RESULT: 3600
EXPECTED: 90000

