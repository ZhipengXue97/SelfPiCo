# Extracted from https://stackoverflow.com/questions/4906977/how-can-i-access-environment-variables-in-python
import os
for a in os.environ:
    print('Var: ', a, 'Value: ', os.getenv(a))
print("all done")

