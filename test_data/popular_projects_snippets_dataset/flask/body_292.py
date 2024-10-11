# Extracted from ./data/repos/flask/src/flask/config.py
"""Updates the values in the config from a Python file.  This function
        behaves as if the file was imported as module with the
        :meth:`from_object` function.

        :param filename: the filename of the config.  This can either be an
                         absolute filename or a filename relative to the
                         root path.
        :param silent: set to ``True`` if you want silent failure for missing
                       files.
        :return: ``True`` if the file was loaded successfully.

        .. versionadded:: 0.7
           `silent` parameter.
        """
filename = os.path.join(self.root_path, filename)
d = types.ModuleType("config")
d.__file__ = filename
try:
    with open(filename, mode="rb") as config_file:
        exec(compile(config_file.read(), filename, "exec"), d.__dict__)
except OSError as e:
    if silent and e.errno in (errno.ENOENT, errno.EISDIR, errno.ENOTDIR):
        exit(False)
    e.strerror = f"Unable to load configuration file ({e.strerror})"
    raise
self.from_object(d)
exit(True)
