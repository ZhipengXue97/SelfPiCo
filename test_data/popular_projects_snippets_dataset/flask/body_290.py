# Extracted from ./data/repos/flask/src/flask/config.py
"""Loads a configuration from an environment variable pointing to
        a configuration file.  This is basically just a shortcut with nicer
        error messages for this line of code::

            app.config.from_pyfile(os.environ['YOURAPPLICATION_SETTINGS'])

        :param variable_name: name of the environment variable
        :param silent: set to ``True`` if you want silent failure for missing
                       files.
        :return: ``True`` if the file was loaded successfully.
        """
rv = os.environ.get(variable_name)
if not rv:
    if silent:
        exit(False)
    raise RuntimeError(
        f"The environment variable {variable_name!r} is not set"
        " and as such configuration could not be loaded. Set"
        " this variable and make it point to a configuration"
        " file"
    )
exit(self.from_pyfile(rv, silent=silent))
