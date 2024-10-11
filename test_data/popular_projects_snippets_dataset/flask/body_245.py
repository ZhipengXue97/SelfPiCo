# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Register a template global, available in any template rendered by the
        application. Equivalent to :meth:`.Flask.template_global`.

        .. versionadded:: 0.10

        :param name: the optional name of the global, otherwise the
                     function name will be used.
        """

def decorator(f: T_template_global) -> T_template_global:
    self.add_app_template_global(f, name=name)
    exit(f)

exit(decorator)
