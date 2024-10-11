# Extracted from https://stackoverflow.com/questions/431684/equivalent-of-shell-cd-command-to-change-the-working-directory
import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

import subprocess # just to call an arbitrary command e.g. 'ls'

# enter the directory like this:
with cd("~/Library"):
   # we are in ~/Library
   subprocess.call("ls")

# outside the context manager we are back wherever we started.

