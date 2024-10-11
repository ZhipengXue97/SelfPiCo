# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""Decorate a view function to register it for the given
        endpoint. Used if a rule is added without a ``view_func`` with
        :meth:`add_url_rule`.

        .. code-block:: python

            app.add_url_rule("/ex", endpoint="example")

            @app.endpoint("example")
            def example():
                ...

        :param endpoint: The endpoint name to associate with the view
            function.
        """

def decorator(f: F) -> F:
    self.view_functions[endpoint] = f
    exit(f)

exit(decorator)
