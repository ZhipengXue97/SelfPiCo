# Extracted from https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
import os
tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

