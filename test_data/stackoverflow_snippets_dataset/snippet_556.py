# Extracted from https://stackoverflow.com/questions/4152963/get-name-of-current-script-in-python
import inspect
source_file_path = inspect.getfile(inspect.currentframe())

import lib_programname
# this returns the fully resolved path to the launched python program
path_to_program = lib_programname.get_path_executed_script()  # type: pathlib.Path

