# Extracted from https://stackoverflow.com/questions/4271740/how-can-i-use-python-to-get-the-system-hostname
import platform
platform.node()

import socket
socket.gethostname()

