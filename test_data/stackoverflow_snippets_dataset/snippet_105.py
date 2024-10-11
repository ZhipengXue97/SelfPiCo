# Extracted from https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
from time import time
start_time = time()
end_time = time()
time_taken = end_time - start_time # time_taken is in seconds
hours, rest = divmod(time_taken,3600)
minutes, seconds = divmod(rest, 60)

