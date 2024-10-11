# Extracted from https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
print("Hello, World!", flush=True)

import sys
sys.stdout.flush()

