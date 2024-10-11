# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Register a template test, available in any template rendered by the
        application. Equivalent to :meth:`.Flask.template_test`.

        .. versionadded:: 0.10

        :param name: the optional name of the test, otherwise the
                     function name will be used.
        """

def decorator(f: T_template_test) -> T_template_test:
    self.add_app_template_test(f, name=name)
    exit(f)

exit(decorator)
