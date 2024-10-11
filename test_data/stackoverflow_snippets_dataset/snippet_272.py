# Extracted from https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
yourProcess.terminate()  # kill the process!

yourThread.daemon = True  # set the Thread as a "daemon thread"

