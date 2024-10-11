# Extracted from https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
import subprocess
subprocess.Popen("cwm --rdf test.rdf --ntriples > test.nt")

