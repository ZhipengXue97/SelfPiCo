# Extracted from https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string
import inspect
import logging
import traceback

def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

def get_function_parameters_and_values():
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    return ([(i, values[i]) for i in args])

def my_func(a, b, c=None):
    logging.info('Running ' + get_function_name() + '(' + str(get_function_parameters_and_values()) +')')
    pass

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] -> %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

my_func(1, 3) # 2016-03-25 17:16:06,927 [INFO] -> Running my_func([('a', 1), ('b', 3), ('c', None)])

