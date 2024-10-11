# Extracted from https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
p.kill()

p = subprocess.Popen("exec " + cmd, stdout=subprocess.PIPE, shell=True)

