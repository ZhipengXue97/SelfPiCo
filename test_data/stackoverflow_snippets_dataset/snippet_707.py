# Extracted from https://stackoverflow.com/questions/6501121/difference-between-exit-and-sys-exit-in-python
exit()

import sys
sys.exit()

import sys
try:
  sys.exit("This is an exit!")
except SystemExit as error:
  print(error)
finally:
  print("Preforming cleanup in 3, 2, 1..")
  # Do code cleanup on exit

