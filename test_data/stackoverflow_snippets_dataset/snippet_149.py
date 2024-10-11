# Extracted from https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
import subprocess
import os
import tempfile

def execute_to_file(command):
    """
    This function execute the command
    and pass its output to a tempfile then read it back
    It is usefull for process that deploy child process
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    path = temp_file.name
    command = command + " > " + path
    proc = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if proc.stderr:
        # if command failed return
        os.unlink(path)
        return
    with open(path, 'r') as f:
        data = f.read()
    os.unlink(path)
    return data

if __name__ == "__main__":
    path = "Somepath"
    command = 'ecls.exe /files ' + path
    print(execute(command))

