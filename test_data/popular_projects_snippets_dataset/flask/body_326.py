# Extracted from ./data/repos/flask/src/flask/cli.py
try:
    __import__(module_name)
except ImportError:
    # Reraise the ImportError if it occurred within the imported module.
    # Determine this by checking whether the trace has a depth > 1.
    if sys.exc_info()[2].tb_next:
        raise NoAppException(
            f"While importing {module_name!r}, an ImportError was"
            f" raised:\n\n{traceback.format_exc()}"
        ) from None
    elif raise_if_not_found:
        raise NoAppException(f"Could not import {module_name!r}.") from None
    else:
        exit()

module = sys.modules[module_name]

if app_name is None:
    exit(find_best_app(module))
else:
    exit(find_app_by_string(module, app_name))
