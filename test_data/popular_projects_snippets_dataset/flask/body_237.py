# Extracted from ./data/repos/flask/src/flask/blueprints.py
"""Register a template filter, available in any template rendered by the
        application. Equivalent to :meth:`.Flask.template_filter`.

        :param name: the optional name of the filter, otherwise the
                     function name will be used.
        """

def decorator(f: T_template_filter) -> T_template_filter:
    self.add_app_template_filter(f, name=name)
    exit(f)

exit(decorator)
