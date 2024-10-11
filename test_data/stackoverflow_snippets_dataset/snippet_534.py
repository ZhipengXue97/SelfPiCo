# Extracted from https://stackoverflow.com/questions/743806/how-do-i-split-a-string-into-a-list-of-words
import shlex
shlex.split("sudo echo 'foo && bar'")
['sudo', 'echo', 'foo && bar']

